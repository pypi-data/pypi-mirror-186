# %%
# Loading libraries
# Libraries For Row-wise data transformation
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Setting up RowStandardScaler
class RowStandardScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.scaler = StandardScaler()

    def fit(self, X: np.ndarray, y=None) -> 'RowStandardScaler':
        """
        Fit scaler on X.
        Transpose X to scale rows instead of columns
        """
        X = X.T
        self.scaler.fit(X)
        return self

    def transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        Apply the scaler to X.
        Transpose X to scale rows instead of columns
        """
        X = X.T
        X_scaled = self.scaler.transform(X)
        return X_scaled.T

    def fit_transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        Fit to data, then transform it.
        """
        return self.fit(X).transform(X)

# Setting up RowMinMaxScaler
class RowMinMaxScaler(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.scaler = MinMaxScaler()

    def fit(self, X: np.ndarray, y=None):
        """
        Fit scaler on X.
        Transpose X to scale rows instead of columns
        """
        X = X.T
        self.scaler.fit(X)
        return self

    def transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        Apply the scaler to X.
        Transpose X to scale rows instead of columns
        """
        X = X.T
        X_scaled = self.scaler.transform(X)
        return X_scaled.T

    def fit_transform(self, X: np.ndarray, y=None) -> np.ndarray:
        """
        Fit to data, then transform it.
        """
        return self.fit(X).transform(X)