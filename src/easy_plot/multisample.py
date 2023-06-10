from logging import getLogger
from typing import Optional, Union

import numpy as np
import pandas as pd
import seaborn as sns  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from matplotlib.patches import PathPatch, Rectangle  # type: ignore
from statsmodels.stats.multicomp import pairwise_tukeyhsd  # type: ignore

from easy_plot.cld import adjgraph_from_tukey, get_cld_from_graph

logger = getLogger(__name__)


def box_swarm_plot(
    df: pd.DataFrame,
    ax: Axes,
    x: str = "group",
    y: str = "value",
    hue: Optional[str] = None,
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    colors: Optional[list[str]] = None,
    color_palette: Optional[str] = None,
    xlabel: Optional[str] = None,
    xlabel_rotation: Optional[float] = None,
    ylabel: Optional[str] = None,
    run_tukey=True,
):
    palette: Optional[Union[str, list[str]]] = None
    if colors is not None and color_palette is not None:
        logger.warn("color_palette is ignoring because colors are specified.")
        palette = colors
    elif colors is not None:
        palette = colors
    elif color_palette is not None:
        palette = color_palette
    else:
        pass

    legend = None
    if hue is not None:
        legend = False

    sns.swarmplot(x=x, y=y, hue=hue, dodge=True, data=df, alpha=0.7, ax=ax, palette=palette)
    sns.boxplot(x=x, y=y, hue=hue, data=df, ax=ax, boxprops=dict(alpha=0.3), palette=palette)
    ax.get_legend().remove()
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    ax.set_ylim(ymin=vmin, ymax=vmax)

    if xlabel_rotation is not None:
        ax.tick_params(axis="x", rotation=xlabel_rotation)

    if run_tukey:
        if hue is None:
            result = pairwise_tukeyhsd(endog=df[y], groups=df[x])
            g = adjgraph_from_tukey(result)
            cld_dict = get_cld_from_graph(g)
            for i, group in enumerate(df[x].unique()):
                y_value = df[df[x] == group][y].quantile(0.9) + 0.1
                ax.text(
                    x=i,
                    y=y_value,
                    s=cld_dict[group],
                    ha="center",
                    fontsize=20,
                    fontweight="bold",
                )
        else:
            df["group"] = df[x] + "_" + df[hue]
            result = pairwise_tukeyhsd(endog=df[y], groups=df["group"])
            g = adjgraph_from_tukey(result)
            cld_dict = get_cld_from_graph(g)

            # Rectangle patches are not included in the list of patches
            patches = [p for p in ax.patches if isinstance(p, PathPatch)]

            for group, box in zip(df["group"].unique(), patches):
                y_value = df[df["group"] == group][y].quantile(0.9) + 0.1
                ax.text(
                    # PathPatch6, so need to unique x values
                    x=np.unique(box.get_path().vertices[:, 0]).mean(),
                    y=y_value,
                    s=cld_dict[group],
                    ha="center",
                    fontsize=20,
                    fontweight="bold",
                )

    return ax
