from logging import getLogger
from typing import Optional, Union

import pandas as pd
import seaborn as sns  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from statsmodels.stats.multicomp import pairwise_tukeyhsd  # type: ignore

from easy_plot.cld import adjgraph_from_tukey, get_cld_from_graph

logger = getLogger(__name__)


def box_swarm_plot(
    df: pd.DataFrame,
    ax: Axes,
    x: str = "group",
    y: str = "value",
    colors: Optional[list[str]] = None,
    color_palette: Optional[str] = None,
    xlabel: Optional[str] = None,
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

    sns.swarmplot(x=x, y=y, data=df, alpha=0.7, ax=ax, palette=palette)
    sns.boxplot(x=x, y=y, data=df, ax=ax, boxprops=dict(alpha=0.3), palette=palette)

    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if run_tukey:
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

    return ax
