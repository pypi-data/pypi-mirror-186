import re
from typing import List, Optional, Tuple

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

from regression_model.config.core import config


def check_stoichiometry(composition):
    elem_counts = re.findall("[0-9]+", composition)
    elem_counts = [int(num) for num in elem_counts]
    return sum(elem_counts) == 40


def drop_na_inputs(*, input_data: pd.DataFrame) -> pd.DataFrame:
    """Check model inputs for na values and filter."""
    validated_data = input_data.copy()

    validated_data = validated_data.fillna(0)

    return validated_data


def validate_inputs(*, input_data: pd.DataFrame) -> Tuple[pd.DataFrame, Optional[dict]]:
    """Check model inputs for unprocessable values."""

    relevant_data = input_data[config.model_config.input_features].copy()

    try:
        if relevant_data[config.model_config.no_nulls_allowed].isnull().values.any():
            raise ValueError("Nulls present in required features.")

        for a_site in config.model_config.a_site_cols:
            elems = relevant_data[a_site].dropna()

            if not (elems.isin(config.model_config.a_site_elements)).min():
                raise ValueError(
                    f"Some elements in {a_site} is not present in the Shannon radius directory."
                )

        for b_site in config.model_config.b_site_cols:
            elems = relevant_data[b_site].dropna()
            if not (elems.isin(config.model_config.b_site_elements)).min():
                raise ValueError(
                    f"Some elements in {b_site} is not present in the Shannon radius directory."
                )

        if (
            not relevant_data[config.model_config.composition]
            .apply(check_stoichiometry)
            .min()
        ):
            raise ValueError("Perovskite oxide is not stoichiometric.")

        validated_data = drop_na_inputs(input_data=relevant_data)
        errors = None

        # replace numpy nans so that pydantic can validate
        MultiplePerovskiteOxideSchema(
            inputs=validated_data.replace({np.nan: None}).to_dict(orient="records")
        )

    except ValidationError as error:
        validated_data = None
        errors = error.json()

    except ValueError as error:
        validated_data = None
        errors = str(error)

    return validated_data, errors


class PerovskiteOxideSchema(BaseModel):
    COMPOSITION: str
    A_SITE_1: str
    A_SITE_2: Optional[str]
    A_SITE_3: Optional[str]
    B_SITE_1: str
    B_SITE_2: Optional[str]
    B_SITE_3: Optional[str]
    NUM_ELEMS: int


class MultiplePerovskiteOxideSchema(BaseModel):
    inputs: List[PerovskiteOxideSchema]
