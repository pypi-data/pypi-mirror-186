import typing as t

import pandas as pd

from regression_model import __version__ as _version
from regression_model.config.core import config
from regression_model.processing.data_manager import load_pipeline
from regression_model.processing.validation import validate_inputs


def make_prediction(
    *,
    input_data: t.Union[pd.DataFrame, dict],
) -> dict:
    """Make a prediction using a saved model pipeline."""

    pipeline_file_name = f"{config.app_config.pipeline_save_file}.pkl"
    formation_energy_pipe = load_pipeline(file_name=pipeline_file_name)

    data = pd.DataFrame(input_data)
    validated_data, errors = validate_inputs(input_data=data)
    results = {"predictions": None, "version": _version, "errors": errors}

    if not errors:
        predictions = formation_energy_pipe.predict(
            X=validated_data[config.model_config.input_features]
        )
        results = {
            "predictions": predictions,
            "version": _version,
            "errors": errors,
        }

    return results
