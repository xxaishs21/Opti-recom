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
G0 = nx.planted_partition_graph(3, 9, 0.3, 0.01, seed=42, directed=True)

# Applique les deux stratégies
G_liens = reco_link_go(G0)                 
G_inter = reco_interests_go(G0)   

print(f"\n Moyenne sur {N} essais")
print_metrics("Graphe initial", init)
print_metrics("Recommandation par liens", liens)
print_metrics("Recommandation par interets", interets)

pos = nx.spring_layout(G0, seed=42, k=0.3)

# Affichage
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
graphs = [G0, G_liens, G_inter]
titles = ["Graphe orienté initial", "Recommandations par liens", "Recommandation par intérêts"]
colors = ["skyblue", "limegreen", "orange"]

for i in range(3):
    ax = axes[i]
    G = graphs[i]
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors[i], node_size=300)

    # --- ICI : on affiche des flèches ---
    nx.draw_networkx_edges(
        G,
        pos,
        ax=ax,
        edge_color=colors[i],
        width=0.8,
        arrows=True,
        arrowstyle='-|>',       # forme de la flèche
        arrowsize=12,           # taille de la flèche
        connectionstyle='arc3,rad=0.05'  # léger arrondi pour mieux voir les arcs
    )
    # ------------------------------------

    nx.draw_networkx_labels(G, pos, ax=ax, font_size=7)
    ax.set_title(titles[i])
    ax.axis('off')

plt.tight_layout()
plt.show()
