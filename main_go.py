import sys
import random

import networkx as nx
from matplotlib import pyplot as plt

from reco_interest import reco_interests_go
from reco_link import reco_link_go
from metrics import modularity, get_metrics, moyenne_sur_essais, print_metrics

#________________________________________________________________________________________________________________

N = 30
init, liens, interets = moyenne_sur_essais(N)

# énère le graphe de base
G0 = nx.planted_partition_graph(3, 10, 0.3, 0.25, seed=42, directed=True)

# Applique les deux stratégies
G_liens = reco_link_go(G0, seuil=3)                 
G_inter = reco_interests_go(G0, seuil=0.35, d=12)   

print(f"\n Moyenne sur {N} essais")
print_metrics("Graphe initial", init)
print_metrics("Recommandation par liens", liens)
print_metrics("Recommandation par interets", interets)

pos = nx.spring_layout(G0, seed=42, k=0.3)

# Affichage
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
