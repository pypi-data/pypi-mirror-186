"""Transformer function library."""
import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin


class DateTransformer(BaseEstimator, TransformerMixin):
    """Feature Extraction for date values."""

    def extract(self, X, y=None):
        """Feature extraction."""
        days = X.dt.dayofyear.values
        days = days.repeat(12).reshape(-1, 12)

        # Starting day of every month
        m_array = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        # How wide the distribution should be
        sigma = 100
        diff = (days - m_array) % 365

        # Normal distribution for continuity of values between month borders
        res = np.exp((-1 / (2 * sigma)) * (diff**2))
        res = pd.DataFrame(res, columns=[f"{X.name}___{str(i)}" for i in range(12)])
        return res

    def fit(self, X, y=None):
        """Fit function."""
        return self

    def transform(self, X, y=None):
        """Transform function."""
        res = []
        for col in X.columns:
            res += [self.extract(pd.to_datetime(X[col], errors="coerce"))]
        res = pd.concat(res, axis=1).fillna(0)
        return res


class GroupbyTransformer(TransformerMixin):
    """Groupby transfomer that groups by index and applies function. Works only with 1 dimensional index."""

    def __init__(self, groupby_func):
        """Initialize."""
        self.groupby_func = groupby_func

    def fit(self, X, y=None, **fit_params):
        """Fit function."""
        self.index = fit_params["index"]
        return self

    def transform(self, X, y=None, **fit_params):
        """Transform function."""
        if isinstance(X, pd.DataFrame):
            X = X.values

        res = pd.DataFrame(X, index=fit_params["index"])
        return res.groupby(level=0).agg(self.groupby_func, axis=1)


class FeatureCrosser(TransformerMixin):
    """Feature Cross transfomer."""

    def __init__(self):
        """Initialize."""

    def fit(self, X, y=None, **fit_params):
        """Fit function."""
        return self

    def transform(self, X, y=None, **fit_params):
        """Transform function."""
        res = []
        for i in range(len(X.columns)):
            for j in range(i + 1, len(X.columns)):
                col_i = X.columns[i]
                col_j = X.columns[j]
                res += [
                    pd.Series(
                        X[col_i].astype(str) + X[col_j].astype(str),
                        name=f"{col_i}___{col_j}",
                    )
                ]
        res = pd.concat(res, axis=1)
        res.index = X.index

        return res
