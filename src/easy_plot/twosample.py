from logging import getLogger
from typing import Literal, Optional, Union

import pandas as pd
import seaborn as sns  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from statannotations.Annotator import Annotator  # type: ignore

logger = getLogger(__name__)


def box_swarm_plot(
    df: pd.DataFrame,
    ax: Axes,
    x: str = "group",
    y: str = "value",
    vmin: Optional[float] = None,
    vmax: Optional[float] = None,
    colors: Optional[list[str]] = None,
    color_palette: Optional[str] = None,
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    test: Optional[Literal["t-test_welch"]] = "t-test_welch",
    text_format: Literal["simple", "star"] = "simple",
):
    groups = list(df[x].unique())
    assert len(groups) == 2

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

    ax.set_ylim(ymin=vmin, ymax=vmax)

    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if test is not None:
        pairs = [(groups[0], groups[1])]
        annotator = Annotator(ax, pairs, data=df, x=x, y=y)
        annotator.configure(test=test, text_format=text_format)
        annotator.apply_and_annotate()

    return ax
