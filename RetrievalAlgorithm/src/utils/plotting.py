import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import List, Dict


def plot_describe_heatmaps(
    dfs: dict,
    stats=('mean', 'std', '25%', '50%', '75%', 'max', 'min'),
    figsize=(14, 6),
    cmap='viridis',
    x_label: str = '',
    y_label: str = '',
    fig_title: str = '',
):
    describe_tables = {}
    global_min, global_max = np.inf, -np.inf

    # Compute describe tables and global color scale
    for name, df in dfs.items():
        desc = df.describe().loc[list(stats)]
        describe_tables[name] = desc
        global_min = min(global_min, desc.values.min())
        global_max = max(global_max, desc.values.max())

    n = len(describe_tables)

    fig, axes = plt.subplots(
        1, n,
        figsize=figsize,
        sharey=True,
        constrained_layout=True
    )

    if n == 1:
        axes = np.array([axes])

    for ax, (name, table) in zip(axes, describe_tables.items()):
        sns.heatmap(
            table,
            ax=ax,
            cmap=cmap,
            vmin=global_min,
            vmax=global_max,
            cbar=ax is axes[-1],
            annot=True,
            fmt='.2f'
        )
        ax.set_title(name)
        # Remove individual x and y labels
        ax.set_xlabel('')
        ax.set_ylabel('')

    if x_label:
        fig.supxlabel(x_label, fontsize=12)
    if y_label:
        fig.supylabel(y_label, fontsize=12)
    if fig_title:
        fig.suptitle(fig_title, fontsize=14)

    return fig



def plot_metrics_at_k(modality_dfs: List[Dict[str, pd.DataFrame]],
                               modality_names: List[str],
                               k_values: List[int] = [5, 10, 20, 50, 100, 200],
                               fig_subtitle: str = 'Precision@k for Different Modalities and Normalizations',
                               y_label: str = 'Precision@k'):
    n_modalities = len(modality_dfs)
    fig, axes = plt.subplots(1, n_modalities, figsize=(6 * n_modalities, 5), sharey=True)

    if n_modalities == 1:
        axes = [axes]  # make it iterable if only one modality

    for ax, dfs, modality_name in zip(axes, modality_dfs, modality_names):
        for norm_name, df in dfs.items():
            mean_values = [df[f'@k{k}'].mean() for k in k_values]
            ax.plot(k_values, mean_values, marker='o', label=norm_name)

        ax.set_title(modality_name)
        ax.set_xlabel('k')
        ax.set_xticks(k_values)
        ax.set_ylim(0, 1)
        ax.grid(True)
        ax.legend()

    axes[0].set_ylabel(y_label)
    plt.suptitle(fig_subtitle)
    plt.tight_layout()

    return fig