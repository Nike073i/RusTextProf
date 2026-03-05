from typing import List, Optional
import pandas as pd
from functools import reduce

class CompositionTransformer:
    def __init__(self, transformers):
        self.transformers = transformers
        
    def transform(self, X):
        return reduce(lambda state, transformer: transformer.transform(state), self.transformers, X)
    
    
class ApplyListTransformer:
    def __init__(self, fn):
        self.fn = fn
        
    def transform(self, X: List) -> List:
        results = []
        for x in X:
            results.append(self.fn(x))
            
        return results
    
    
class DataFrameTransformer:
    def __init__(self, columns):
        self.columns = columns

    def transform(self, X):
        return pd.DataFrame(X, columns=self.columns)


class DefaultValueTransformer:
    def __init__(self, default_val):
        self.default_val = default_val
        
    def transform(self, X):
        return X.fillna(self.default_val)


class RenameColumnTransformer:
    def __init__(self, mapper):
        self.mapper = mapper

    def transform(self, X):
        return X.rename(columns=self.mapper)


class BinarizationRule:
    def __init__(self, 
                 current_name: str, 
                 new_name: str, 
                 between: Optional[List[float]] = None, 
                 gt_then: Optional[float] = None,
                 lt_then: Optional[float] = None):
        self.current_name = current_name
        self.new_name = new_name
        self.between = between
        self.gt_then = gt_then
        self.lt_then = lt_then
        
    def apply(self, series: pd.Series) -> pd.Series:
        if self.between is not None:
            return series.between(self.between[0], self.between[1])
        elif self.gt_then is not None:
            return series > self.gt_then
        elif self.lt_then is not None:
            return series < self.lt_then
        return series
        
        
class BinarizationTransformer:
    def __init__(self, rules: List[BinarizationRule]):
        self.rules = rules

    def transform(self, X):
        for rule in self.rules:
            X[rule.new_name] = rule.apply(X[rule.current_name]).astype(int)
        return X

    
class DropColumnTransformer:
    def __init__(self, columns: List[str]):
        self.columns = columns

    def transform(self, X: pd.DataFrame):
        return X.drop(columns=self.columns)

    
class ModelWrapper:
    def __init__(self, transformer, model):
        self._transformer = transformer
        self._model = model
    
    def predict(self, X):
        x_prepared = self._transformer.transform(X)
        return self._model.predict(x_prepared)
    
    def predict_proba(self, X):
        x_prepared = self._transformer.transform(X)
        return self._model.predict_proba(x_prepared)