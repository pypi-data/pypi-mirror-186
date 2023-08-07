from typing import Union

import numpy as np
import pandas as pd

from insurance_claim_model import __version__
from insurance_claim_model.config.core import TRAINED_MODEL_DIR, config
from insurance_claim_model.processing.data_manager import load_pipeline
from insurance_claim_model.processing.validation import validate_input

pipeline_path = (
    f"{TRAINED_MODEL_DIR}/{config.app_config.pipeline_save_file}-{__version__}.pkl"
)
predict_pipeline = load_pipeline(pipeline_save_file=pipeline_path)


def predict_data(*, input_data: Union[pd.DataFrame, dict]) -> dict:

    input_data = pd.DataFrame(input_data)
    validated_data, errors = validate_input(input_data=input_data)
    results = {"prediction": None, "version": __version__, "errors": errors}

    if not errors:
        predictions = predict_pipeline.predict(validated_data)

        results = {
            "predictions": [np.exp(prediction) for prediction in predictions],  # type: ignore
            "version": __version__,
            "errors": errors,
        }

    return results
