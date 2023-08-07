from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import CategoricalImputer, MeanMedianImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from insurance_claim_model.config.core import config

predict_pipe = Pipeline(
    [
        (
            "frequent_imputation",
            CategoricalImputer(
                imputation_method="frequent", variables=config.model_config.cat_na
            ),
        ),
        (
            "mean_imputation",
            MeanMedianImputer(
                imputation_method="mean", variables=config.model_config.num_na
            ),
        ),
        (
            "categorical_encoder",
            OneHotEncoder(drop_last=True, variables=config.model_config.cat_vars),
        ),
        ("scaler", MinMaxScaler()),
        (
            "RandomForest",
            RandomForestRegressor(
                random_state=config.model_config.random_state,
                n_estimators=config.model_config.n_estimators,
                max_depth=config.model_config.max_depth,
            ),
        ),
    ]
)
