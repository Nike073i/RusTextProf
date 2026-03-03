import pandas as pd
import numpy as np
from sklearn.model_selection import GridSearchCV, learning_curve


def grid_search(model, params, X_train, y_train, **kwargs):
    gs = GridSearchCV(model, params, verbose=1, cv=5, n_jobs=-1)
    gs.fit(X_train, y_train, **kwargs)
    return gs 


def iteration_learning_score(model, X, y, cv=5, scoring='accuracy'):
    train_sizes, train_scores, val_scores = learning_curve(
        model,
        X,
        y,
        train_sizes=np.linspace(0.1, 1.0, 10),
        cv=cv,
        scoring=scoring
    )
    return train_sizes, train_scores, val_scores


def get_top_n_info(gs, n=10):
    return pd.DataFrame(gs.cv_results_).nsmallest(n, 'rank_test_score')
