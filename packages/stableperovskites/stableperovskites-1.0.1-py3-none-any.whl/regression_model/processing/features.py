import re
from typing import List

import numpy as np
import numpy.typing as npt
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

from regression_model.config.core import config


class ReplaceBlank(BaseEstimator, TransformerMixin):
    def __init__(self):
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        X = X.replace(" ", 0)
        X = X.fillna(0)
        return X


class NumOfSites(BaseEstimator, TransformerMixin):
    def __init__(self, sites: List[str]):
        self.sites = sites
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def count_site_nums(self, composition: str, site: str) -> int:
        matches = re.findall(r"(\D*)(\d*)", composition)
        number_of_matches = len(matches)
        if site is not None:
            for j in range(number_of_matches):
                if matches[j][0] == site:
                    return int(matches[j][1])
                else:
                    continue
        return 0

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        for site in self.sites:
            X["NUM_" + site] = X.apply(
                lambda x: self.count_site_nums(x["COMPOSITION"], x[site]), axis=1
            )
        return X


class PopulateElementalProp(BaseEstimator, TransformerMixin):
    def __init__(self, ep: pd.DataFrame, prefixes: List[str], sites: List[str]):
        self.ep = ep
        self.prefixes = prefixes
        self.sites = sites
        return None

    def fit(self, X: pd.DataFrame, y=None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        X[self.sites] = X[self.sites].astype("str")

        for i in range(len(self.prefixes)):
            X = X.merge(
                self.ep.add_prefix(self.prefixes[i] + "_"),
                how="left",
                left_on=self.sites[i],
                right_on=self.prefixes[i] + "_SYMBOL",
            )

        return X


class ShannonRadius(BaseEstimator, TransformerMixin):
    def __init__(
        self,
        a_shan: pd.DataFrame,
        b_shan: pd.DataFrame,
        prefixes: List[str],
        sites: List[str],
    ):
        self.a_shan = a_shan
        self.b_shan = b_shan
        self.a_prefixes = prefixes[0:3]
        self.b_prefixes = prefixes[3:6]
        self.a_sites = sites[0:3]
        self.b_sites = sites[3:6]
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for i in range(len(self.a_prefixes)):

            X = X.merge(
                self.a_shan.add_prefix(self.a_prefixes[i] + "_SHAN_"),
                how="left",
                left_on=self.a_sites[i],
                right_on=self.a_prefixes[i] + "_SHAN_A_SITE",
            )

        for i in range(len(self.b_prefixes)):
            X = X.merge(
                self.b_shan.add_prefix(self.b_prefixes[i] + "_SHAN_"),
                how="left",
                left_on=self.b_sites[i],
                right_on=self.b_prefixes[i] + "_SHAN_B_SITE",
            )

        cols_to_drop = [
            col
            for col in X.columns
            if ("_SHAN_A_SITE" in col) or ("_SHAN_B_SITE" in col)
        ]

        X = X.drop(columns=cols_to_drop)

        return X


class CompositionAveragedProperties(BaseEstimator, TransformerMixin):
    def __init__(self, sites: List[str], ep: pd.DataFrame, prefixes: List[str]):
        self.a_sites = sites[0:3]
        self.b_sites = sites[3:6]
        self.a_num_sites = ["NUM_" + site for site in sites[0:3]]
        self.b_num_sites = ["NUM_" + site for site in sites[3:6]]
        self.ep = ep
        self.prefixes = prefixes
        self.a_props = [""]
        self.b_props = [""]
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def get_wt_avgd_property(
        self, prop: npt.ArrayLike, num_site: npt.ArrayLike
    ) -> float:
        return np.sum(np.multiply(prop, num_site)) / 8

    def get_max(self, sites, num_site):
        return sites[np.argmax(num_site)]

    def all_max(self, triplets: List[float]) -> float:
        return max(triplets)

    def all_min(self, triplets: List[float]) -> float:
        return min(triplets)

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for property in config.model_config.relevant_properties:

            property_list = [prefix + "_" + property for prefix in self.prefixes]

            if property not in ["SHAN_A_RADII", "SHAN_B_RADII"]:
                self.a_props = property_list[0:3]
                self.b_props = property_list[3:6]

                X["A_WT_AVG_" + property] = X.apply(
                    lambda x: self.get_wt_avgd_property(
                        x[self.a_props].fillna(0).to_numpy(),
                        x[self.a_num_sites].fillna(0).to_numpy(),
                    ),
                    axis=1,
                )

                X["A_ALL_MAX_" + property] = X.apply(
                    lambda x: self.all_max(list(x[self.a_props])), axis=1
                )

                X["A_ALL_MIN_" + property] = X.apply(
                    lambda x: self.all_min(list(x[self.a_props])), axis=1
                )

                X["B_WT_AVG_" + property] = X.apply(
                    lambda x: self.get_wt_avgd_property(
                        x[self.b_props].fillna(0).to_numpy(),
                        x[self.b_num_sites].fillna(0).to_numpy(),
                    ),
                    axis=1,
                )

                X["B_ALL_MAX_" + property] = X.apply(
                    lambda x: self.all_max(list(x[self.b_props])), axis=1
                )

                X["B_ALL_MIN_" + property] = X.apply(
                    lambda x: self.all_min(list(x[self.b_props])), axis=1
                )

                X["A_RANGE_" + property] = (
                    X["A_ALL_MAX_" + property] - X["A_ALL_MIN_" + property]
                )
                X["B_RANGE_" + property] = (
                    X["B_ALL_MAX_" + property] - X["B_ALL_MIN_" + property]
                )

            elif property == "SHAN_A_RADII":
                self.a_props = property_list[0:3]
                X["A_WT_AVG_SHAN_A_RADII"] = X.apply(
                    lambda x: self.get_wt_avgd_property(
                        x[self.a_props].fillna(0).to_numpy(),
                        x[self.a_num_sites].fillna(0).to_numpy(),
                    ),
                    axis=1,
                )

                X["A_ALL_MAX_" + property] = X.apply(
                    lambda x: self.all_max(list(x[self.a_props])), axis=1
                )
                X["A_ALL_MIN_" + property] = X.apply(
                    lambda x: self.all_min(list(x[self.a_props])), axis=1
                )
                X["A_RANGE_" + property] = (
                    X["A_ALL_MAX_" + property] - X["A_ALL_MIN_" + property]
                )

            elif property == "SHAN_B_RADII":
                self.b_props = property_list[3:6]
                X["B_WT_AVG_SHAN_B_RADII"] = X.apply(
                    lambda x: self.get_wt_avgd_property(
                        x[self.b_props].fillna(0).to_numpy(),
                        x[self.b_num_sites].fillna(0).to_numpy(),
                    ),
                    axis=1,
                )
                X["B_ALL_MAX_" + property] = X.apply(
                    lambda x: self.all_max(list(x[self.b_props])), axis=1
                )
                X["B_ALL_MIN_" + property] = X.apply(
                    lambda x: self.all_min(list(x[self.b_props])), axis=1
                )
                X["B_RANGE_" + property] = (
                    X["B_ALL_MAX_" + property] - X["B_ALL_MIN_" + property]
                )

        X["A_MAX"] = X.apply(
            lambda x: self.get_max(
                list(x[self.a_sites].fillna(np.nan)),
                list(x[self.a_num_sites].fillna(0)),
            ),
            axis=1,
        )
        X["B_MAX"] = X.apply(
            lambda x: self.get_max(
                list(x[self.b_sites].fillna(np.nan)),
                list(x[self.b_num_sites].fillna(0)),
            ),
            axis=1,
        )

        return X


class PopulateMajorityIonProperties(BaseEstimator, TransformerMixin):
    def __init__(self, ep: pd.DataFrame, cols: List[str]):
        self.ep = ep
        self.cols = cols
        return None

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()

        for col in self.cols:
            X = X.merge(
                self.ep.add_prefix(col + "_"),
                how="left",
                left_on=col,
                right_on=col + "_SYMBOL",
            )

        properties = self.ep.drop(columns=["SYMBOL"]).columns

        for property in properties:
            X["AVG_MAJ_" + property] = X[
                ["A_MAX_" + property, "B_MAX_" + property]
            ].mean(axis=1)
            X["DIFF_MAJ_" + property] = X["A_MAX_" + property] - X["B_MAX_" + property]

        return X


class KeepDesiredFeatures(BaseEstimator, TransformerMixin):
    def __init__(self, features: List[str]):
        self.features = features

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X = X.copy()
        return X[self.features].fillna(0)
