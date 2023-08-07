import os
from pathlib import Path
from typing import List, Text

import joblib
import pandas as pd
from sklearn.pipeline import Pipeline

from insurance_claim_model import __version__
from insurance_claim_model.config.core import DATASET_DIR, TRAINED_MODEL_DIR, config


def load_dataset(*, file_name: Text) -> pd.DataFrame:

    training_path = DATASET_DIR / file_name

    transformed = pd.read_csv(training_path)
    transformed.drop(["index", "PatientID"], axis=1, inplace=True)

    return transformed


def save_pipeline(*, pipeline: Pipeline) -> None:

    pipeline_name = f"{config.app_config.pipeline_save_file}-{__version__}.pkl"
    pipeline_to_persist = TRAINED_MODEL_DIR / pipeline_name

    remove_old_pipeline(files_to_keep=[pipeline_name])
    joblib.dump(pipeline, pipeline_to_persist)


def load_pipeline(*, pipeline_save_file: Text) -> Pipeline:

    pipeline_path = TRAINED_MODEL_DIR / pipeline_save_file
    pipeline = joblib.load(pipeline_path)

    return pipeline


def remove_old_pipeline(*, files_to_keep: List[Text]) -> None:

    files_to_keep = files_to_keep + ["__init__.py"]
    for file in os.listdir(TRAINED_MODEL_DIR):
        if file not in files_to_keep:
            os.unlink(Path(TRAINED_MODEL_DIR / file))
