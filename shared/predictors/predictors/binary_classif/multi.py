from .classifier import Classifier
import numpy as np

class CascadeClassifier(Classifier):
    def __init__(self, pipeline):
        super().__init__(pipeline)
    
    def predict(self, features):
        proba = self.pipeline.predict_proba(features)
        
        return proba[:, 1::2]
    
class FlatClassifier(Classifier):
    def __init__(self, pipeline):
        super().__init__(pipeline)
        
    def predict(self, features):
        proba = self.pipeline.predict_proba(features)
        
        n_classes = proba.shape[1]
        
        n_targets = int(np.log2(n_classes))
        
        result = np.zeros((proba.shape[0], n_targets))
        
        for target_idx in range(n_targets):
            for class_idx in range(n_classes):
                if (class_idx >> (n_targets - 1 - target_idx)) & 1:
                    result[:, target_idx] += proba[:, class_idx]
        
        return result