from lightgbm import LGBMRegressor
from sklearn.pipeline import Pipeline

from regression_model.config.core import config
from regression_model.processing.data_manager import load_dataset
from regression_model.processing.features import (
    CompositionAveragedProperties,
    KeepDesiredFeatures,
    NumOfSites,
    PopulateElementalProp,
    PopulateMajorityIonProperties,
    ReplaceBlank,
    ShannonRadius,
)

elemental_properties = load_dataset(file_name=config.app_config.elemental_prop)
shan_rad = load_dataset(file_name=config.app_config.shan_rad)

a_shan_rad = shan_rad[config.app_config.a_shan_rad_cols].dropna()
b_shan_rad = shan_rad[config.app_config.b_shan_rad_cols].dropna()

formation_energy_pipe = Pipeline(
    [
        ("replace_blank", ReplaceBlank()),
        (
            "populate_elemental_prop",
            PopulateElementalProp(
                ep=elemental_properties,
                prefixes=config.model_config.prefixes,
                sites=config.model_config.site_names,
            ),
        ),
        ("count_num_sites", NumOfSites(sites=config.model_config.site_names)),
        (
            "add_shannon_radius",
            ShannonRadius(
                a_shan=a_shan_rad,
                b_shan=b_shan_rad,
                prefixes=config.model_config.prefixes,
                sites=config.model_config.site_names,
            ),
        ),
        (
            "add_structural_parameters",
            CompositionAveragedProperties(
                sites=config.model_config.site_names,
                ep=elemental_properties,
                prefixes=config.model_config.prefixes,
            ),
        ),
        (
            "populate_majority_ion_properties",
            PopulateMajorityIonProperties(
                ep=elemental_properties, cols=config.model_config.max_cols
            ),
        ),
        (
            "keep_desired_features",
            KeepDesiredFeatures(features=config.model_config.features),
        ),
        ("lgbm_regressor", LGBMRegressor()),
    ]
)
