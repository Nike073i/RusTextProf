
import numpy as np

def split(df, n=10):
    return np.array_split(df.index, n)

def fold_scores(fn, y_true, y_pred, n_folds=10):
    folds = split(y_true, n=n_folds)
    
    return [ fn(y_true[fold], y_pred[fold]) for fold in folds ]
    