import sys
import locale

from matplotlib import pyplot as plt
import networkx as nx
import numpy as np
from copy import deepcopy
import networkx.algorithms.community as nx_comm #fct de détection de communautés dans les graphes

from find_cycle_gno import cycle_list
from reco_interest import reco_interests_gno
from reco_link import reco_link_gno

from metrics import modularity, get_metrics, moyenne_sur_essais, print_metrics


N = 30
init, liens, interets = moyenne_sur_essais(N)

print(f"\n Moyenne sur {N} essais")
print_metrics("Graphe initial", init)
print_metrics("Recommandation par liens", liens)
print_metrics("Recommandation par interets", interets)

# Génère le graphe de base
G0 = nx.random_partition_graph([10]*5, 0.3, 0.001)
print(G0)# 5 composantes, peu connectées

# Applique les deux stratégies
G1 = reco_link_gno(deepcopy(G0))
G2 = reco_interests_gno(deepcopy(G0))

# Calcule une position fixe plus compacte
pos = nx.spring_layout(G0, seed=42, k=0.3)  # k plus petit = nœuds plus proches

# Prépare l'affichage
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
graphs = [G0, G1, G2]
titles = ['Graphe initial', 'Recommandation par liens', 'Recommandation par intérêts']
colors = ['skyblue', 'limegreen', 'orange']

for i in range(3):
    ax = axes[i]
    G = graphs[i]
    nx.draw_networkx_nodes(G, pos, ax=ax, node_color=colors[i], node_size=300)
    nx.draw_networkx_edges(G, pos, ax=ax, edge_color=colors[i], width=0.8)
    nx.draw_networkx_labels(G, pos, ax=ax, font_size=7)
    ax.set_title(titles[i])
    ax.axis('off')

plt.tight_layout()
plt.show()