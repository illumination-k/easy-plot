from argparse import Namespace
from typing import Optional

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd

from easy_plot import multisample, twosample


def get_figsize(s: Optional[str]):
    if s is None:
        return None
    else:
        return eval(s)


def plot_multisample(args: Namespace):
    df = pd.read_csv(args.input, header=None)
    df.columns = pd.Index(["group", "value"])
    fig = plt.figure(figsize=get_figsize(args.figsize))
    ax = fig.add_subplot(111)
    multisample.box_swarm_plot(
        df,
        ax,
        xlabel=args.xlabel,
        ylabel=args.ylabel,
        run_tukey=args.run_tukey,
        colors=args.colors,
    )

    plt.savefig(args.output)


def plot_twosample(args: Namespace):
    df = pd.read_csv(args.input, header=None)
    df.columns = pd.Index(["group", "value"])
    fig = plt.figure(figsize=get_figsize(args.figsize))
    ax = fig.add_subplot(111)
    twosample.box_swarm_plot(
        df,
        ax,
        xlabel=args.xlabel,
        ylabel=args.ylabel,
        test=args.test,
        text_format=args.text_format,
        colors=args.colors,
    )

    plt.savefig(args.output)
