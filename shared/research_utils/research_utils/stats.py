import pandas as pd
from scipy.stats import levene

def agg_by_columns(df, cols, fn, **fnargs):
    results = []
    for col in cols:
        results.append(fn(df[col], **fnargs))

    return pd.DataFrame(results, index=cols)
    
def cv_score(std, mean):
    return std / mean * 100

def levene_test(subgroups, critical=0.05):
    stat, p_value = levene(*subgroups)
    return pd.Series({
        'p_value': p_value,
        'levene_statistic': stat,
        'stability': p_value > critical
    })
