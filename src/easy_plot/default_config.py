import matplotlib as mpl  # type: ignore
import matplotlib.font_manager as font_manager  # type: ignore
import matplotlib.pyplot as plt  # type: ignore

fontpaths = ["/mnt/c/Windows/Fonts"]

font_files = font_manager.findSystemFonts(fontpaths=fontpaths)
for font_file in font_files:
    font_manager.fontManager.addfont(font_file)

plt.rcParams["font.family"] = "Arial"

mpl.rcParams["pdf.fonttype"] = 42
mpl.rcParams["ps.fonttype"] = 42

plt.rcParams["font.size"] = 15
plt.rcParams["xtick.direction"] = "in"  # x axis in
plt.rcParams["ytick.direction"] = "in"  # y axis in
plt.rcParams["axes.linewidth"] = 1.0  # axis line width
