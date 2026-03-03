from sklearn.base import BaseEstimator, TransformerMixin


class ModelFeatureSelector(BaseEstimator, TransformerMixin):
    def __init__(self, keys):
        self.keys = keys
    
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        return X[self.keys]