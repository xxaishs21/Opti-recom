import sys
import random
random.seed(42)  # reproductibilité pour les intérêts aléatoires

import networkx as nx
from matplotlib import pyplot as plt

from reco_interest import reco_interests_go
from reco_link import reco_link_go

# 1) Graphe de base non orienté puis conversion en DiGraph (symétrisation des arêtes)
G0_undirected = nx.random_partition_graph([7]*3, 0.3, 0.25, seed=42)
G0 = nx.DiGraph()
G0.add_nodes_from(G0_undirected.nodes())
G0.add_edges_from((u, v) for u, v in G0_undirected.edges())
G0.add_edges_from((v, u) for u, v in G0_undirected.edges())

# 2) Recommandations orientées avec seuils réajustés
G_liens = reco_link_go(G0, seuil=3)                 # un peu plus strict que 2
G_inter = reco_interests_go(G0, seuil=0.35, d=12)   # plus permissif pour des vecteurs 0/1 aléatoires

# 3) Mise en page partagée
pos = nx.spring_layout(G0_undirected, seed=42, k=0.3)

# 4) Affichage
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
graphs = [G0, G_liens, G_inter]
titles = ["Graphe initial (orienté)", "Après reco par liens", "Après reco par intérêts"]
colors = ["skyblue", "limegreen", "orange"]

for ax, G, title, color in zip(axes, graphs, titles, colors):
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=color, node_size=250)
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=color, width=0.9, alpha=0.9, arrows=False)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()
