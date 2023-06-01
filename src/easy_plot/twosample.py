from typing import Literal, Optional

import pandas as pd
import seaborn as sns  # type: ignore
from matplotlib.axes import Axes  # type: ignore
from statannotations.Annotator import Annotator  # type: ignore


def box_swarm_plot(
    df: pd.DataFrame,
    ax: Axes,
    x: str = "group",
    y: str = "value",
    xlabel: Optional[str] = None,
    ylabel: Optional[str] = None,
    test: Optional[Literal["t-test_welch"]] = "t-test_welch",
    text_format: Literal["simple", "star"] = "simple",
):
    assert len(df[x].unique()) == 2

    sns.swarmplot(x=x, y=y, data=df, alpha=0.7, ax=ax)
    sns.boxplot(x=x, y=y, data=df, ax=ax, boxprops=dict(alpha=0.3))

    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)

    if test is not None:
        pairs = [(x, y)]
        annotator = Annotator(ax, pairs, data=df, x=x, y=y)
        annotator.configure(test="t-test_welch", text_format=text_format)
        annotator.apply_and_annotate()

    return ax
