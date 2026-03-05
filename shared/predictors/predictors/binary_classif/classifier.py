from abc import ABC, abstractmethod
import pandas as pd
import numpy as np
    
class Classifier(ABC):
    def __init__(self, pipeline):
        self.pipeline = pipeline
    
    @abstractmethod
    def predict(self, features: pd.DataFrame) -> np.ndarray:
        raise NotImplementedError() 
