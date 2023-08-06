import numpy as np
import pandas as pd
from catboost import CatBoostClassifier
from sklearn.base import BaseEstimator, ClassifierMixin


class CatRF(BaseEstimator, ClassifierMixin):
    """A Random Forest made of CatboostClassifiers. Only applicable for binary classification."""

    def __init__(self, n_cats=30, **catboost_kwargs):
        """Instantiate number of cats and base architecture of CatboostClassifier."""
        self.n_cats = n_cats
        self.estimators = [
            CatBoostClassifier(random_state=ri, **catboost_kwargs)
            for ri in range(n_cats)
        ]

    def fit(self, X, y, **fit_params):
        """Fit individual cat."""
        for clf in self.estimators:
            clf.fit(X, y, **fit_params)

        # Set feature importance with format like other Sklearn's classifiers
        self.feature_names_ = X.columns
        feature_importances = self.get_feature_importance()
        feature_importances = feature_importances.reindex(self.feature_names_)
        self.feature_importances_ = feature_importances.values
        return self

    def predict_proba(self, X):
        """Take mean of all cat's predictions."""
        pred = [clf.predict_proba(X[clf.feature_names_]) for clf in self.estimators]
        pred = np.mean(pred, axis=0)
        assert len(pred) == len(X)
        return pred

    def get_feature_importance(self) -> pd.Series:
        """Get mean of feature importances from all cats."""
        feature_importance_lists = [
            pd.Series(model.feature_importances_, index=model.feature_names_)
            for model in self.estimators
        ]
        return (
            pd.concat(feature_importance_lists, axis=1)
            .mean(axis=1)
            .sort_values(ascending=False)
        )
