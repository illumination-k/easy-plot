from typing import Literal, Optional

from pydantic import BaseModel


class Config(BaseModel):
    font_paths: list[str] = []
    font_family: Optional[str] = None

    font_size: int = 15
    xtick_direction: Literal["in", "out"] = "in"
    ytick_direction: Literal["in", "out"] = "in"
    axes_line_width: float = 1.0

    def apply_config(self):
        import matplotlib.font_manager as font_manager  # type: ignore
        import matplotlib.pyplot as plt  # type: ignore

        fontpaths = self.font_paths

        font_files = font_manager.findSystemFonts(fontpaths=fontpaths)
        for font_file in font_files:
            font_manager.fontManager.addfont(font_file)

        if self.font_family is not None:
            plt.rcParams["font.family"] = self.font_family

        plt.rcParams["font.size"] = self.font_size
        plt.rcParams["xtick.direction"] = self.xtick_direction  # x axis in
        plt.rcParams["ytick.direction"] = self.ytick_direction  # y axis in
        plt.rcParams["axes.linewidth"] = self.axes_line_width  # axis line width

    @staticmethod
    def apply_from_path(path: Optional[str]):
        import json

        if path:
            with open(path) as f:
                Config(**json.load(f)).apply_config()
        else:
            Config().apply_config()
