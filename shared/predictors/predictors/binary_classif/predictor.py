from dataclasses import dataclass
from .classifier import Classifier

@dataclass
class ClassPrediction:
    proba: float
    threshold: float
    label: str

class Predictor:
    def __init__(self, classifier: Classifier, thresholds, labels):
        self.classifier = classifier
        self.thresholds = thresholds
        self.labels = labels
        
    def predict(self, features):
        proba = self.classifier.predict(features)
        
        result = []
        for sample in proba:
            sample_predictions = []
            for i, (threshold, label_pair) in enumerate(zip(self.thresholds, self.labels)):
                pred = ClassPrediction(
                    proba=sample[i].item(),
                    threshold=threshold,
                    label=label_pair[0] if sample[i] < threshold else label_pair[1]
                )
                sample_predictions.append(pred)
            result.append(sample_predictions)
        
        return result