from pathlib import Path
from typing import Dict, List, Optional

import yaml
from pydantic import BaseModel

import insurance_claim_model

PACKAGE_ROOT = Path(insurance_claim_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):

    package_name: str
    training_data_file: str
    testing_data_file: str
    pipeline_save_file: str


class ModelConfig(BaseModel):

    cat_na: List[str]
    num_na: List[str]
    cat_vars: List[str]
    num_vars: List[str]
    drop_columns: List[str]
    target: str
    test_size: float
    random_state: int
    n_estimators: int
    max_depth: int


class Config(BaseModel):
    app_config: AppConfig
    model_config: ModelConfig


def find_config_file() -> Path:

    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH

    raise Exception(f"Config file is not at this path: {CONFIG_FILE_PATH}")


def fetch_config_file(cfg_path: Optional[Path] = None) -> Dict:

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path) as conf_file:
            config = yaml.safe_load(conf_file)
        return config

    raise Exception(f"Config file is not at this path: {CONFIG_FILE_PATH}")


def create_and_validate_config(parsed_config: Optional[Dict] = None) -> Config:

    if parsed_config is None:
        parsed_config = fetch_config_file(CONFIG_FILE_PATH)

    _config = Config(
        app_config=AppConfig(**parsed_config), model_config=ModelConfig(**parsed_config)
    )

    return _config


config = create_and_validate_config()
