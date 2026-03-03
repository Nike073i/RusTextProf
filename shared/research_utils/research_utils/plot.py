import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def create_panel(n, cols=3, row_width=16, row_height=5):
    n_rows = math.ceil(n / cols)
    fig, axes = plt.subplots(n_rows, cols, figsize=(row_width, row_height * n_rows))    
    
    if isinstance(axes, plt.Axes):
        axes = np.array([[axes]])

    return fig, axes

def plot_learning_curve(train_sizes, train_scores, val_scores, ax, train_color='blue', val_color='green', score_color='red', name=""):
    train_mean = np.mean(train_scores, axis=1)
    train_std = np.std(train_scores, axis=1)
    val_mean = np.mean(val_scores, axis=1)
    val_std = np.std(val_scores, axis=1)
    best_score = np.max(val_mean)
    
    ax.plot(train_sizes, train_mean, 'o-', color=train_color, label=f'Training score {name}', linewidth=2)
    ax.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, 
                     alpha=0.15, color=train_color)
    
    ax.plot(train_sizes, val_mean, 'o-', color=val_color, label=f'Cross-validation score {name}', linewidth=2)
    ax.fill_between(train_sizes, val_mean - val_std, val_mean + val_std, 
                     alpha=0.15, color=val_color)
    
    ax.axhline(y=best_score, color=score_color, linestyle='--', 
                label=f'Best CV score {name}: {best_score:.3f}')
    
    ax.set_xlabel('Training examples')
    ax.set_ylabel('Accuracy')
    ax.legend(loc='best')
    ax.grid(True, alpha=0.3)
    
def plot_complexity_and_accuracy(gs):
    results = pd.DataFrame(gs.cv_results_)
    
    plt.figure(figsize=(10, 6))
    
    scatter = plt.scatter(results['mean_test_score'], 
                         results['mean_fit_time'],
                         c=results['rank_test_score'], 
                         cmap='viridis_r',
                         alpha=0.6, 
                         s=100)
    
    cbar = plt.colorbar(scatter)
    cbar.set_label('Ранг модели')
    
    plt.xlabel('Средняя точность (Accuracy)')
    plt.ylabel('Среднее время обучения (сек)')
    plt.title('Компромисс: точность vs время обучения')
    
    best_idx = results['rank_test_score'].argmin()
    
    plt.annotate('Лучшая модель', 
                (results.loc[best_idx, 'mean_test_score'], 
                 results.loc[best_idx, 'mean_fit_time']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=12, fontweight='bold')
    
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def series_hist(series, title, ax, bins=50, lower_quantile=0.02, upper_quantile=0.98):
    if lower_quantile is None:
        lower_quantile = 0
    if upper_quantile is None:
        upper_quantile = 1
    
    lower_bound = series.quantile(lower_quantile)
    upper_bound = series.quantile(upper_quantile)
    filtered_data = series[series.between(lower_bound, upper_bound)]
    filtered_data.plot(kind="hist", ax=ax, title=title, bins=bins)

def series_scatter(series_a, series_b, titles, ax, lowess=True, line_kws=None, corr_method="spearman", **kwargs):
    if line_kws is None:
        line_kws = {'color': 'red', 'linewidth': 2}

    sns.scatterplot(x=series_a, y=series_b, alpha=0.5, s=30, ax=ax, **kwargs)
    sns.regplot(x=series_a, y=series_b, scatter=False, lowess=lowess,
                line_kws=line_kws, ax=ax)

    ax.set_title(f'{titles[0]} vs {titles[1]}')
    ax.set_xlabel(titles[0])
    ax.set_ylabel(titles[1])

    if corr_method:
        corr = series_b.corr(series_a, method=corr_method)
        ax.text(0.05, 0.95, f'ρ = {corr:.3f}',
                transform=ax.transAxes,
                bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

def df_plot(df, selectors, plot, axes, **pltargs):
    if axes.size < len(selectors):
        raise ValueError(f"Несоответствие кол-во axes ({axes.size}) и данных ({len(selectors)})")

    for idx, selector in enumerate(selectors):
        data = selector(df)
        ax = axes.flat[idx]                
        plot(*data, ax, **pltargs)

    for idx in range(len(selectors), axes.size):
        axes.flat[idx].set_visible(False)

def df_hist(df, cols, axes, **pltargs):
    selectors = [lambda df, col=col: (df[col], col) for col in cols]
    df_plot(df, selectors, series_hist, axes, **pltargs)

def df_scatter(df, pairs, axes, **pltargs):
    selectors = [lambda df, col1=col1, col2=col2: (df[col1], df[col2], [col1, col2]) 
                 for col1, col2 in pairs]
    df_plot(df, selectors, series_scatter, axes, **pltargs)
