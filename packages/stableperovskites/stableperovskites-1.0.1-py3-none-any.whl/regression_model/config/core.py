from pathlib import Path
from typing import List

from pydantic import BaseModel
from strictyaml import YAML, load

import regression_model

# Project Directories
PACKAGE_ROOT = Path(regression_model.__file__).resolve().parent
ROOT = PACKAGE_ROOT.parent
CONFIG_FILE_PATH = PACKAGE_ROOT / "config.yml"
DATASET_DIR = PACKAGE_ROOT / "datasets"
TRAINED_MODEL_DIR = PACKAGE_ROOT / "trained_models"


class AppConfig(BaseModel):
    """
    Application-level config.
    """

    package_name: str
    pipeline_save_file: str
    dft_calc_train: str
    dft_calc_test: str
    dft_calc_test_validation: str
    elemental_prop: str
    shan_rad: str
    a_shan_rad_cols: List[str]
    b_shan_rad_cols: List[str]
    no_nulls_in_required_loc: int
    a_site_not_present_loc: int
    b_site_not_present_loc: int
    non_stoichiometric_loc: int
    replace_blank_col: str
    replace_blank_loc: int
    num_site_test_col: str
    num_site_test_loc: int
    populate_elem_col: str
    populate_elem_loc: int
    a_shannon_radius_col: str
    a_shannon_radius_loc: int
    b_shannon_radius_col: str
    b_shannon_radius_loc: int
    comp_avgd_cols: List[str]
    comp_avgd_loc: int
    comp_avgd_expected_vals: List[float]
    avg_maj_col: str
    diff_maj_col: str
    avg_maj_loc: int
    diff_maj_loc: int
    test_split: str


class ModelConfig(BaseModel):
    """
    All configuration relevant to model
    training and feature engineering.
    """

    target: str
    features: List[str]
    test_size: float
    random_state: int
    remove_comma: str
    col_names_no_symbol: List[str]
    site_names: List[str]
    prefixes: List[str]
    elemental_property_cols: List[str]
    a_site_elements: List[str]
    b_site_elements: List[str]
    no_nulls_allowed: List[str]
    input_features: List[str]
    max_cols: List[str]
    composition: str
    relevant_properties: List[str]
    a_site_cols: List[str]
    b_site_cols: List[str]


class Config(BaseModel):
    """Master config object."""

    app_config: AppConfig
    model_config: ModelConfig


def find_config_file() -> Path:
    """
    Locate the configuration file.
    """

    if CONFIG_FILE_PATH.is_file():
        return CONFIG_FILE_PATH
    raise Exception(f"Config not found at {CONFIG_FILE_PATH!r}")


def fetch_config_from_yaml(cfg_path: Path = None) -> YAML:
    """
    Parse YAML containing the package configuration.
    """

    if not cfg_path:
        cfg_path = find_config_file()

    if cfg_path:
        with open(cfg_path, "r") as conf_file:
            parsed_config = load(conf_file.read())
            return parsed_config
    raise OSError(f"Did not find config file at path: {cfg_path}")


def create_and_validate_config(parsed_config: YAML = None) -> Config:
    """
    Run validation on config values.
    """

    if parsed_config is None:
        parsed_config = fetch_config_from_yaml()

    # specify the data attribute from the strictyaml YAML type.
    _config = Config(
        app_config=AppConfig(**parsed_config.data),
        model_config=ModelConfig(**parsed_config.data),
    )

    return _config


config = create_and_validate_config()
