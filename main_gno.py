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


#Calculer la modularité
def modularity(G):
    communities = list(nx_comm.greedy_modularity_communities(G))
    return nx_comm.modularity(G, communities)

#Calculer les métriques
def get_metrics(G):
    return {
        "edges": G.number_of_edges(),
        "cycles": len(cycle_list(G)),
        "clustering": nx.average_clustering(G),
        "components": nx.number_connected_components(G),
        "modularity": modularity(G)
    }


# Fonction principale : moyenne des métriques sur plusieurs essais
def moyenne_sur_essais(N=30, n=50, k=3, p=0.05):
    stats_initial = []
    stats_liens = []
    stats_interets = []

    for _ in range(N):
        G0 = nx.relaxed_caveman_graph(l=n // k, k=k, p=0.05)  

        stats_initial.append(get_metrics(G0))

        G1 = reco_link_gno(deepcopy(G0))
        stats_liens.append(get_metrics(G1))

        G2 = reco_interests_gno(deepcopy(G0))
        stats_interets.append(get_metrics(G2))


    def moyenne(stats):
        return {k: np.mean([d[k] for d in stats]) for k in stats[0]}

    return (
        moyenne(stats_initial),
        moyenne(stats_liens),
        moyenne(stats_interets)
    )

def print_metrics(title, stats, color="🔵"):
    print(f"{color} {title}")
    print(f"   ↪ Nombre d’arêtes        : {stats['edges']:.1f}")
    print(f"   ↪ Clustering coefficient  : {stats['clustering']:.3f}")
    print(f"   ↪ Composantes connexes    : {stats['components']:.1f}")
    print(f"   ↪ Modularity              : {stats['modularity']:.3f}")
    print()



N = 30
init, liens, interets = moyenne_sur_essais(N)

"""
print(f"\n 📊 Moyenne sur {N} essais")
print_metrics("Graphe initial", init, "🔵")
print_metrics("Recommandation par liens", liens, "🟢")
print_metrics("Recommandation par intérêts", interets, "🟠")
"""


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
