import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
from statsmodels.sandbox.stats.multicomp import TukeyHSDResults
import networkx as nx

# https://qiita.com/TomosurebaOrange/items/c28fc9cae922f3c21e08

def adjgraph_from_tukey(result: TukeyHSDResults) -> nx.Graph:
    df = pd.read_csv(io.StringIO(result.as_csv()), skiprows=1, skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    g = nx.Graph()
    for _, row in df.iterrows():
        if row["reject"].strip() == "False":
            g.add_edge(row["group1"], row["group2"])
        else:
            g.add_node(row["group1"])
            g.add_node(row["group2"])

    return g

def get_cld_from_graph(g: nx.Graph) -> dict[str, str]:
    cliques = nx.find_cliques(g)

    labels = list(g.nodes())
    # 各クリーク集合の要素について，同一の文字列ラベルを与える
    cld_dict = {label: [] for label in labels}
    for i, clique in enumerate(cliques):
        letter = chr(i + 97)
        for j in clique:
            cld_dict[j].append(letter)

    for i in cld_dict:
        cld_dict[i] = ''.join(cld_dict[i])

    return cld_dict