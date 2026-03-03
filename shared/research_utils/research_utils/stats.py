import pandas as pd
import numpy as np
from scipy.stats import levene, mannwhitneyu, chi2_contingency
from statsmodels.regression.mixed_linear_model import MixedLM

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

def constant_ratio_iqr(series, iqr_ratio=0.1):
    result = {}
    
    median = series.median()
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    
    result['comp_iqr'] = iqr
    result['median'] = median
    
    if iqr == 0:
        unique_values = series.sort_values().unique()
        if len(unique_values) > 1:
            min_diff = np.min(np.diff(unique_values))
            iqr = min_diff
        else:
            result['usage_iqr'] = 0
            result['lower_bound'] = median
            result['upper_bound'] = median
            result['in_interval_ratio'] = 1
            return result
        
    result['usage_iqr'] = iqr
    
    lower_bound = median - iqr_ratio * iqr
    upper_bound = median + iqr_ratio * iqr
    
    result['lower_bound'] = lower_bound
    result['upper_bound'] = upper_bound
    
    
    in_interval = ((series >= lower_bound) & (series <= upper_bound)).sum()
    result['in_interval_ratio'] = in_interval / len(series)
    
    return result

def u_test(series_a, series_b, alpha=0.001):
    stat, p_value = mannwhitneyu(series_a, series_b)

    a_med = series_a.median()
    b_med = series_b.median()
    diff_med = abs(a_med - b_med)

    return { 
        "U-критерий": stat,
        "P-значение": p_value,
        "Различие": p_value < alpha,
        "Размер выборки А": len(series_a),
        "Размер выборки Б": len(series_b),
        "Медиана А": a_med,
        "Медиана А": a_med,
        "Медиана Б": b_med,
        "Разница медиан": diff_med
    }
    
def chi2_test(series_x, series_y, alpha=0.05):
    crosstab = pd.crosstab(series_x, series_y)

    chi2, p, dof, expected = chi2_contingency(crosstab)

    expected_flat = expected.flatten()
    small_cells = sum(expected_flat < 5)
    total_cells = len(expected_flat)
    percent_small = (small_cells / total_cells) * 100
    warning = ""
    if percent_small > 20:
        warning = (f"Предупреждение: {small_cells} из {total_cells} ячеек "
                   f"({percent_small:.1f}%) имеют ожидаемую частоту < 5.\n"
                   "Результаты могут быть неточными. Рекомендуется точный тест Фишера.")

    significant = p < alpha

    return {
        "Хи-квадрат": chi2,
        "P-значение": p,
        "Различие": significant,
        "Предупреждение": warning
    }
    
def icc_test(group_col, data, metric_col):
    def interpret_icc(icc):
        if pd.isna(icc):
            return "Ошибка расчета"
        elif icc < 0.2:
            return "Очень низкая схожесть"
        elif icc < 0.4:
            return "Низкая схожесть"
        elif icc < 0.6:
            return "Умеренная схожесть"
        elif icc < 0.8:
            return "Высокая схожесть"
        else:
            return "Очень высокая схожесть"
        
    model = MixedLM.from_formula(
        f"{metric_col} ~ 1",
        groups=data[group_col],
        re_formula="1",
        data=data
    )
    result = model.fit(reml=True, method='bfgs')
    
    var_between = result.cov_re.iloc[0, 0]
    var_within = result.scale
    var_total = var_between + var_within
    icc = var_between / var_total if var_total > 0 else 0
    
    return {
        'metric': metric_col,
        'icc': icc,
        'var_between': var_between,
        'var_within': var_within,
        'var_total': var_total,
        'converged': result.converged,
        "interpretation": interpret_icc(icc)
    }