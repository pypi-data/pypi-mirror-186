import hashlib
import parse
import re
import logging
import json

import cv2
import numpy as np
import pandas as pd
from functools import wraps
from tqdm import tqdm
from pydantic import BaseModel, Field
from io import BytesIO
from typing import ClassVar, Any, Dict
from enum import Enum


from brevettiai.io.path import join as join_path
from brevettiai.platform import Dataset
from brevettiai.data.image.annotation_parser import expand_samples_with_annotations
from brevettiai.data.image import ImageKeys
from brevettiai.data.tf_types import TfRange, SequenceShape
from brevettiai.data.inspection_info import InspectionType, inspection_view_map
import concurrent.futures

log = logging.getLogger(__name__)


@parse.with_pattern(r'(.+)', regex_group_count=1)
def match_all(text):
    return text


FRAME_DEFERENCE = re.compile(r"{frame(:.+)?}")

sequence_shape_columns = [
    "sequence_shape_frames",
    "sequence_shape_height",
    "sequence_shape_width",
    "sequence_shape_channels",
]


def get_annotation_fix_workflow(dataset):
    """Get function to fix annotations in dataset"""
    def fix_annotations(x):
        targets = {}
        for ix, row in x.iterrows():
            path = BcimgDatasetSamples.build_annotation_path(bucket=dataset.bucket,
                                                             path_format=row.annotation_relpath, **row)
            annotation = json.loads(dataset.io.read_file(path, cache=False))
            items = len(annotation["annotations"])
            targets[path] = items
        targets = pd.Series(targets).sort_values(ascending=False)
        for i, (k, v) in enumerate(targets.items()):
            op = "delete" if i else "keep"
            print(f"{op} {k} with {v} annotations")
        answer = input("Perform operations [y/n]")
        if answer.lower() == "y":
            for k, v in targets.iloc[1:].items():
                print(f"Removing {k}")
                dataset.io.remove(k)
            return True
        return False

    return fix_annotations


class BcimgDatasetSamples(BaseModel):
    SAMPLES_FILE: ClassVar[str] = "bcimg_dataset_index.csv"

    sequence_window: int = Field(default=3, description="Size of window range")
    filter: Dict[str, Any] = Field(default_factory=dict)

    def _index_file_path(self, dataset):
        return dataset.get_location("samples", self.SAMPLES_FILE)

    def is_valid_dataset(self, dataset):
        return dataset.io.isfile(self._index_file_path(dataset))

    def _get_sequences_from_dataset(self, dataset: Dataset, annotations=True, duplicates=False, cache=False):
        if not self.is_valid_dataset(dataset):
            log.warning(f"dataset '{dataset.name}' is not valid - {dataset.get_uri()}")
            return pd.DataFrame()

        # Read index
        buf = BytesIO(dataset.io.read_file(self._index_file_path(dataset), cache=cache))
        df = pd.read_csv(buf, dtype={"sample_id": str})

        # Map data
        df["sequence_shape"] = df[sequence_shape_columns].apply(lambda x: SequenceShape(*x), axis=1)
        df = df.drop(sequence_shape_columns, axis=1, errors="coerce")

        if "inspection" in df:
            df["camera_view"] = df["inspection"].map(inspection_view_map)

        for k, v in self.filter.items():
            if k not in df:
                return pd.DataFrame()
            if isinstance(v, str):
                df = df[~df[k].isna() & df[k].str.match(v)]
            elif isinstance(v, list):
                df = df[df[k].isin(v)]
            else:
                df = df[df[k] == v]

        df["bucket"] = dataset.bucket
        df["dataset_id"] = dataset.id
        df["dataset"] = dataset.name

        if annotations:
            if df.empty:
                log.warning(f"{dataset.name} - {dataset.get_uri()}: Contains no valid samples")
                df["annotation_frames"] = np.nan
                df["annotation_names"] = np.nan
                return df

            annotations = dataset.get_annotations(filter=None)

            # Check if format of first (all) sequences has a frame number and indexes accordingly
            head_fields = parse.compile(df.path_format.iloc[0]).named_fields
            no_frame = "frame" not in head_fields
            if no_frame:
                df["aindex"] = df.path_format
                annotations.index = annotations.folder
            else:
                df["aindex"] = pd.Index(df.path_format.str.extract("(.+){frame(?:.+)?}(.+)"))
                annotations.index = pd.Index(annotations.folder.str.extract(r"(.+[_/\\(?frame)])\d+(.+)"))

            # Extract info from dataframe
            annotations["annotation_name"] = annotations["path"].str.extract(r".+[\\/](.+\.json)")
            annotations["annotation_relpath"] = annotations["folder"]

            # Check duplicates
            if not duplicates:
                duplicate_mask = annotations.folder.duplicated(keep=False)
                if duplicate_mask.any():
                    print("Duplicate annotations detected, initiating fixing mode")
                    fixed = annotations[duplicate_mask].groupby("folder").apply(get_annotation_fix_workflow(dataset))
                    if fixed.all():
                        return self._get_sequences_from_dataset(dataset, True, False, cache)
                    else:
                        assert duplicate_mask.any() == False, \
                            f"{dataset.name}: " + "\n".join(x for x in annotations[duplicate_mask].annotation_relpath)

            # Reverse merge formatter onto annotations
            pf = df.path_format
            pf.index = df.aindex
            annotations = annotations.join(pf, how="inner")

            if annotations.empty:
                log.warning(f"{dataset.name} - {dataset.get_uri()}: Contains no valid annotations")
                df["annotation_frames"] = np.nan
                df["annotation_names"] = np.nan
                return df

            # Extract frame number
            if no_frame:
                annotations["frame"] = 0
            else:
                annotations["frame"] = annotations.apply(
                    lambda x: parse.parse(x.path_format, x.annotation_relpath)["frame"], axis=1)

            # Group and collect information
            seq_ann = annotations.groupby(level=0).agg(
                annotation_frames=("frame", lambda x: x.to_list()),
                annotation_names=("annotation_name", lambda x: x.to_list()),
            )

            # Join onto samples dataframe
            df = df.join(seq_ann, on="aindex")
            df.drop("aindex", errors="coerce", axis=1, inplace=True)
        return df

    @wraps(_get_sequences_from_dataset)
    def get_sequences(self, datasets, **kwargs):
        if isinstance(datasets, Dataset):
            return self._get_sequences_from_dataset(datasets, **kwargs)

        with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
            futures = [executor.submit(self._get_sequences_from_dataset, ds, **kwargs)
                       for ds in sorted(datasets, key=lambda x: x.id)]
        return pd.concat([f.result() for f in futures]).reset_index(drop=True)

    def expand_sequences_with_annotations(self, df):
        # Explode samples
        frames = df.annotation_frames.explode()
        names = df.annotation_names.explode()
        samples = df[[x for x in df.columns if x not in {"annotation_frames", "annotation_names"}]].reindex(
            frames.index)
        samples["frame"] = frames
        samples["annotation_name"] = names

        # Build paths
        samples[ImageKeys.SEQUENCE_RANGE] = samples.frame.apply(self.get_range_fn())
        samples["annotation_path"] = samples.apply(lambda x: BcimgDatasetSamples.build_annotation_path(**x), axis=1)
        return samples

    def expand_annotations_files(self, samples):
        samples = samples.reset_index(drop=False)
        samples = expand_samples_with_annotations(samples, key="annotation_path")
        samples.set_index(samples.columns[0], drop=True, inplace=True)
        # remove samples with empty annotation files
        samples = samples[~samples["type"].isna()]
        samples = samples.drop("features", errors="ignore", axis=1)
        if "is_hole" in samples.columns:
            samples["is_hole"] = samples["is_hole"].map({np.nan: -1, False: 0, True: 1}).astype(int)
        return samples

    def get_range_fn(self):
        _before = self.sequence_window // 2
        _after = self.sequence_window - _before

        def get_range(x):
            return TfRange(x - _before, x + _after)

        return get_range

    @staticmethod
    def _get_sequence_shape_from_group(dataset, grouper):
        frames = grouper.frame.max() + 1
        path = grouper.path.head(1).iloc[0]
        shape = cv2.imdecode(np.frombuffer(dataset.io.read_file(path), np.uint8), -1).shape
        # create shape with extra channel and slice, because image shape may be only two dimensional for 1 channel
        return SequenceShape(*(frames, *shape, 1)[:4])

    def _update_sequence_index_for_dataset(self, dataset, path_format,
                                           tv_inspection_map: Dict[str, InspectionType] = None,
                                           extra_info=None, drop_columns=None, dry_run=False):
        log.info(f"Updating index for {dataset.name}")

        extra_info = extra_info or {}
        samples = dataset.get_image_samples()
        samples["relpath"] = samples.path.str[len(dataset.bucket) + 1:]

        path_pattern = parse.compile(path_format, {"all": match_all})
        parse_results = samples.relpath.apply(lambda x: path_pattern.parse(x))
        no_parse_mask = parse_results.isna()
        for danger in samples.path[no_parse_mask]:
            log.warning(f"Skipping sample which does not match format {danger}")
        samples, parse_results = samples[~no_parse_mask], parse_results[~no_parse_mask]
        assert parse_results.empty is False, "Dataset does not contain any samples matching parsing format."
        info = pd.DataFrame.from_records(parse_results.apply(lambda x: x.named).values)
        path_format_clean = path_format.replace(":all}", "}")

        if "frame" not in path_pattern.named_fields:
            log.warning("frame not detected in format, Assuming all images are single frame sequences")
            info["frame"] = 0

        grpcols = info[[c for c in info.columns if c != "frame"]]
        info.index = pd.Index(grpcols)
        samples.index = info.index
        samples["frame"] = info["frame"]
        samples_grouper = samples.groupby(level=0)
        info_grouper = info.groupby(level=0)

        tqdm.pandas(desc="Cleaning path_format")
        path_format_clean = info_grouper[grpcols.columns].head(1).progress_apply(
            lambda x: self.build_path(bucket=None, path_format=path_format_clean, **x), axis=1)
        tqdm.pandas(desc="Getting sequence etag")
        etag = samples_grouper.etag.progress_apply(lambda x: f"{hashlib.md5(''.join(x).encode()).hexdigest()}-{len(x)}")

        for k, v in extra_info.items():
            if callable(v):
                tqdm.pandas(desc=f"Extracting extra_info for {k}")
                extra_info[k] = info_grouper.progress_apply(v)

        tqdm.pandas(desc="Loading sequence shapes")
        sequence_shape = samples_grouper.progress_apply(lambda g: self._get_sequence_shape_from_group(dataset, g))
        _sequence_shape = pd.DataFrame(index=sequence_shape.index,
                                       data=sequence_shape.apply(tuple).to_list(),
                                       columns=sequence_shape_columns)

        df = pd.DataFrame(
            data={
                **info_grouper[grpcols.columns].head(1),
                "path_format": path_format_clean,
                "etag": etag,
                **_sequence_shape,
                **extra_info,
            }
        ).reset_index(drop=True)

        # extract inspection
        if tv_inspection_map is not None:
            df["inspection"] = df.tv.apply(lambda x: tv_inspection_map[x].value)

        # Ensure inspection is string
        df["inspection"] = df["inspection"].apply(lambda x: x.value if isinstance(x, Enum) else str(x))

        if drop_columns is not None:
            df = df.drop(drop_columns, axis=1)

        if not dry_run:
            dataset.upload(self._index_file_path(dataset), df.to_csv(index=False))

        return df

    @wraps(_update_sequence_index_for_dataset)
    def update_sequence_index(self, datasets, **kwargs):
        if isinstance(datasets, Dataset):
            datasets = [datasets]
        return pd.concat([self._update_sequence_index_for_dataset(dataset, **kwargs) for dataset in datasets])

    @staticmethod
    def build_path(bucket, path_format, frame=None, **kwargs):
        if frame is None:
            path_format = re.sub(FRAME_DEFERENCE, r"{{frame\1}}", path_format)

        relpath = path_format.format(frame=frame, **kwargs)
        if bucket is None:
            return relpath
        return join_path(bucket, relpath)

    @staticmethod
    def build_annotation_path(bucket, path_format, annotation_name, frame=None, **kwargs):
        if frame is None:
            path_format = re.sub(FRAME_DEFERENCE, r"{{frame\1}}", path_format)

        relpath = path_format.format(frame=frame, **kwargs)
        if bucket is None:
            return relpath
        return join_path(bucket, ".annotations", relpath, annotation_name)
