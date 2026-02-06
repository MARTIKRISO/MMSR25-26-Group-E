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
    decimal_positions: int = 2
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
            fmt=f'.{decimal_positions}f'
        )
        ax.set_title(name)
        # Remove individual x and y labels
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(axis='x', labelrotation=90)

    if x_label:
        fig.supxlabel(x_label, fontsize=12)
    if y_label:
        fig.supylabel(y_label, fontsize=12)
    if fig_title:
        fig.suptitle(fig_title, fontsize=14)

    return fig


def plot_rs_type_means(
        modality_dfs: Dict[str, List[pd.DataFrame]],
        figsize=(14, 6),
        cmap='viridis',
        x_label: str = '',
        y_label: str = '',
        fig_title: str = '',
        decimal_positions: int = 2
):
    heatmap_data = {}

    for rs_type, df_dict in modality_dfs.items():
        if not isinstance(df_dict, dict):
            raise ValueError(f"Expected dict of DataFrames for RS type '{rs_type}', got {type(df_dict)}")

        combined_means = []
        for df in df_dict.values():
            if not isinstance(df, pd.DataFrame):
                raise ValueError(f"Expected DataFrame in '{rs_type}', got {type(df)}")
            combined_means.append(df.mean())

        # Concatenate all means into a single series for this RS type
        combined_mean_series = pd.concat(combined_means, axis=0)
        heatmap_data[rs_type] = combined_mean_series

    # Convert to DataFrame for heatmap
    heatmap_df = pd.DataFrame(heatmap_data).T.fillna(0)

    # Determine global color scale
    vmin, vmax = heatmap_df.values.min(), heatmap_df.values.max()

    # Plot heatmap
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(
        heatmap_df,
        ax=ax,
        cmap=cmap,
        vmin=vmin,
        vmax=vmax,
        annot=True,
        fmt=f'.{decimal_positions}f',
        cbar=True
    )

    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    if fig_title:
        ax.set_title(fig_title)

    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    fig.tight_layout()
    return fig



def plot_metrics_at_k(modality_dfs: List[Dict[str, pd.DataFrame]],
                               modality_names: List[str],
                               k_values: List[int] = [5, 10, 20, 50, 100, 200],
                               fig_subtitle: str = 'Precision@k for Different Modalities and Normalizations',
                               y_label: str = 'Precision@k',
                               y_lim_low: float = 0,
                               y_lim_high: float = 1,
                        ):
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
        ax.set_ylim(y_lim_low, y_lim_high)
        ax.grid(True)
        ax.legend()

    axes[0].set_ylabel(y_label)
    plt.suptitle(fig_subtitle)
    plt.tight_layout()

    return fig


def plot_describe_heatmaps_nn(
        nn_variations: dict,
        stats=('mean', 'std', '25%', '50%', '75%', 'max', 'min'),
        figsize=(14, 8),
        cmap='viridis',
        x_label: str = '',
        y_label: str = '',
        fig_title: str = '',
        decimal_positions: int = 2
):
    describe_tables = {}
    global_min, global_max = np.inf, -np.inf

    # Compute describe tables and global color scale
    for name, df in nn_variations.items():
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
            fmt=f'.{decimal_positions}f'
        )
        ax.set_title(name)
        ax.set_xlabel('')
        ax.set_ylabel('')
        ax.tick_params(axis='x', labelrotation=90)

    if x_label:
        fig.supxlabel(x_label, fontsize=12)
    if y_label:
        fig.supylabel(y_label, fontsize=12)
    if fig_title:
        fig.suptitle(fig_title, fontsize=14)

    return fig


from typing import Dict, List

def plot_metrics_at_k_nn(
    nn_variation_dfs: Dict[str, pd.DataFrame],
    k_values: List[int] = [5, 10, 20, 50, 100, 200],
    fig_subtitle: str = 'Precision@k for Different NN Embedding Variations',
    y_label: str = 'Precision@k',
    y_lim_low: float = 0,
    y_lim_high: float = 1,
):
    fig, ax = plt.subplots(figsize=(10, 6))

    for variation_name, df in nn_variation_dfs.items():
        mean_values = [df[f'@k{k}'].mean() for k in k_values]
        ax.plot(k_values, mean_values, marker='o', label=variation_name)

    ax.set_xlabel('k')
    ax.set_ylabel(y_label)
    ax.set_xticks(k_values)
    ax.set_ylim(y_lim_low, y_lim_high)
    ax.grid(True)
    ax.legend()
    ax.set_title(fig_subtitle)
    plt.tight_layout()

    return fig


def plot_rs_heatmaps_means(
    modality_dfs: dict,
    figsize=(18, 8),
    cmap='viridis',
    x_label: str = '',
    y_label: str = '',
    fig_title: str = '',
    decimal_positions: int = 2
):
    norm_names = sorted({norm for df_dict in modality_dfs.values() for norm in df_dict.keys()})
    n_norms = len(norm_names)

    fig, axes = plt.subplots(
        1, n_norms,
        figsize=figsize,
        constrained_layout=True,
        sharey=True
    )

    if n_norms == 1:
        axes = [axes]

    # Global color scale
    all_values = []
    for norm_name in norm_names:
        for rs_type, df_dict in modality_dfs.items():
            df = df_dict.get(norm_name)
            if df is None:
                continue
            numeric_df = df.select_dtypes(include=np.number)
            if not numeric_df.empty:
                all_values.append(numeric_df.mean().values)
    vmin, vmax = (np.min(np.concatenate(all_values)), np.max(np.concatenate(all_values))) if all_values else (0,1)

    for i, norm_name in enumerate(norm_names):
        ax = axes[i]
        heatmap_data = {}
        for rs_type, df_dict in modality_dfs.items():
            df = df_dict.get(norm_name)
            if df is None:
                continue
            numeric_df = df.select_dtypes(include=np.number)
            if numeric_df.empty:
                continue
            heatmap_data[rs_type] = numeric_df.mean()
        heatmap_df = pd.DataFrame(heatmap_data).T.fillna(0)
        sns.heatmap(
            heatmap_df,
            ax=ax,
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot=True,
            fmt=f'.{decimal_positions}f',
            cbar=i==n_norms-1
        )
        ax.set_title(f'Normalization: {norm_name}', fontsize=12)
        ax.set_yticks(np.arange(len(heatmap_df.index)) + 0.5)
        ax.set_yticklabels(heatmap_df.index, rotation=0, fontsize=10)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
        ax.set_xlabel(x_label if i==n_norms-1 else '')
        ax.set_ylabel(y_label if i==0 else '')

    if fig_title:
        fig.suptitle(fig_title, fontsize=16, y=1.03)

    return fig


def plot_nn_heatmaps_means(
    nn_variations: dict,
    figsize=(18, 6),
    cmap='viridis',
    x_label: str = '',
    y_label: str = '',
    fig_title: str = '',
    decimal_positions: int = 2
):

    nn_names = list(nn_variations.keys())
    n_nn = len(nn_names)

    fig, axes = plt.subplots(
        1, n_nn,
        figsize=figsize,
        constrained_layout=True,
        sharey=True
    )

    if n_nn == 1:
        axes = [axes]

    # Global color scale
    all_values = []
    for variations_dict in nn_variations.values():
        for df in variations_dict.values():
            numeric_df = df.select_dtypes(include=np.number)
            if not numeric_df.empty:
                all_values.append(numeric_df.mean().values)
    vmin, vmax = (np.min(np.concatenate(all_values)), np.max(np.concatenate(all_values))) if all_values else (0,1)

    # Plot each NN type
    for i, nn_name in enumerate(nn_names):
        ax = axes[i]
        variations_dict = nn_variations[nn_name]

        # Compute mean per variation
        heatmap_rows = []
        row_labels = []
        for var_name, df in variations_dict.items():
            numeric_df = df.select_dtypes(include=np.number)
            if numeric_df.empty:
                continue
            heatmap_rows.append(numeric_df.mean().values)  # mean across columns
            row_labels.append(var_name)  # save variation names

        # Build DataFrame: rows = variations, columns = metrics
        heatmap_df = pd.DataFrame(heatmap_rows, index=row_labels, columns=numeric_df.columns)

        sns.heatmap(
            heatmap_df,
            ax=ax,
            cmap=cmap,
            vmin=vmin,
            vmax=vmax,
            annot=True,
            fmt=f'.{decimal_positions}f',
            cbar=i==n_nn-1
        )

        # Titles and axis labels
        ax.set_title(nn_name, fontsize=12)
        ax.set_xlabel(x_label if i == n_nn-1 else '')

        # Y-axis labels: show only on first subplot
        if i == 0:
            ax.set_ylabel(y_label, fontsize=10)
            ax.set_yticklabels(heatmap_df.index, rotation=0, fontsize=10)
        else:
            ax.set_ylabel('')
            # ax.set_yticklabels([])

        # X-axis labels
        ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    if fig_title:
        fig.suptitle(fig_title, fontsize=16, y=1.03)

    return fig

