import argparse

from easy_plot import handlers
from easy_plot.config import Config


def attach_plot_argument(parser: argparse.ArgumentParser):
    parser.add_argument(
        "--figsize", type=str, default=None, help="Figsize of plot. write tuple value like (10, 10)"
    )
    parser.add_argument(
        "--xlabel", type=str, default=None, help="xlabel of figure. default is group"
    )
    parser.add_argument(
        "--ylabel", type=str, default=None, help="ylabel of figure. default is value"
    )
    parser.add_argument("--colors", nargs="*", default=None, help="specify a color of each group")

    return parser


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", default=None, type=str)

    subparsers = parser.add_subparsers()
    multisample_parser = subparsers.add_parser("multisample")
    multisample_parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=str,
        help="input csv file. First row should be group label and second row should be value",
    )
    multisample_parser.add_argument(
        "-o", "--output", required=True, type=str, help="Ouput image path"
    )
    multisample_parser.add_argument(
        "--run-tukey", action="store_false", help="Run pairwise_tukey or not"
    )

    multisample_parser = attach_plot_argument(multisample_parser)

    multisample_parser.set_defaults(handler=handlers.plot_multisample)

    twosample_parser = subparsers.add_parser("twosample")
    twosample_parser.add_argument(
        "-i",
        "--input",
        required=True,
        type=str,
        help="input csv file. First row should be group label and second row should be value. These is just two group labels!",
    )
    twosample_parser.add_argument(
        "-o", "--output", required=True, type=str, help="Ouput image path"
    )
    twosample_parser.add_argument("--test", choices=["t-test_welch"], default="t-test_welch")
    twosample_parser.add_argument("--text-format", choices=["simple", "star"], default="simple")

    twosample_parser = attach_plot_argument(twosample_parser)

    twosample_parser.set_defaults(handler=handlers.plot_twosample)

    args = parser.parse_args()

    if hasattr(args, "handler"):
        Config.apply_from_path(args.config)
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
