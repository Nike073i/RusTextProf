import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

class CascadedClassifier(BaseEstimator, ClassifierMixin):
    def __init__(self, main_clf, secondary_clf, threshold=0.5):
        self.main_clf = main_clf
        self.secondary_clf = secondary_clf
        self.threshold = threshold

    def fit(self, X, y):
        raise NotImplementedError("Модель уже обучена, fit не требуется.")

    def predict(self, X):
        main_pred = self.main_clf.predict(X)
        secondary_pred = np.empty(X.shape[0], dtype=int)

        for i, clf in enumerate(self.secondary_clf):
            cls_idx = main_pred == i
            if np.any(cls_idx):
                secondary_pred[cls_idx] = clf.predict(X[cls_idx])

        return np.column_stack([main_pred, secondary_pred])

    def predict_proba(self, X):
        main_proba = self.main_clf.predict_proba(X)
        main_pred = (main_proba[:, 1] >= self.threshold).astype(int)

        secondary_proba = np.zeros((X.shape[0], 2))

        for i, clf in enumerate(self.secondary_clf):
            idx = main_pred == i
            if np.any(idx):
                secondary_proba[idx] = clf.predict_proba(X[idx])

        return np.hstack([main_proba, secondary_proba])