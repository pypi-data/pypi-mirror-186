from typing import Dict, List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from insurance_claim_model.config.core import config


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:

    data = input_data.copy()
    new_na_columns = [
        var
        for var in data.columns
        if var not in config.model_config.cat_na
        and var not in config.model_config.num_na
        and data[var].isnull().sum() > 0
    ]

    data.dropna(subset=new_na_columns, inplace=True)

    return data


def validate_input(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[Dict]]:

    validated_data = drop_na_inputs(input_data=input_data)
    errors = None

    try:
        MultipleInsuranceInputs(
            inputs=validated_data.replace({np.nan, None}).to_dict(orient="records")
        )
    except ValidationError as error:
        errors = error.json()

    return validated_data, errors


class InsuranceDataInputScheme(BaseModel):

    age: Optional[Union[float, int]]
    gender: Optional[str]
    bmi: Optional[float]
    bloodpressure: Optional[int]
    diabetic: Optional[str]
    children: Optional[int]
    smoker: Optional[str]
    region: Optional[str]
    claim: Optional[float]


class MultipleInsuranceInputs(BaseModel):
    inputs: List[InsuranceDataInputScheme]
