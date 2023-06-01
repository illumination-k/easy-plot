from argparse import Namespace

import matplotlib.pyplot as plt  # type: ignore
import pandas as pd

from easy_plot import multisample, twosample


def plot_multisample(args: Namespace):
    df = pd.read_csv(args.input, header=None)
    df.columns = pd.Index(["group", "value"])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    multisample.box_swarm_plot(
        df, ax, xlabel=args.xlabel, ylabel=args.ylabel, run_tukey=args.run_tukey
    )

    plt.savefig(args.output)


def plot_twosample(args: Namespace):
    df = pd.read_csv(args.input, header=None)
    df.columns = pd.Index(["group", "value"])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    twosample.box_swarm_plot(
        df, ax, xlabel=args.xlabel, ylabel=args.ylabel, test=args.test, text_format=args.text_format
    )

    plt.savefig(args.output)
