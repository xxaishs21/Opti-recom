import networkx as nx
import numpy as np
import networkx.algorithms.community as nx_comm
import copy 

from reco_link import reco_link_go
from find_cycle_go import cycle_list
from reco_interest import reco_interests_go

#________________________________________________________________________________________________________________

#Calculer la modularité
def modularity(G):
    communities = list(nx_comm.greedy_modularity_communities(G))
    return nx_comm.modularity(G, communities)

#Calculer le nombre de composantes connexes
def get_metrics(G):
    if G.is_directed():
        nb_comp = nx.number_weakly_connected_components(G)
    else:
        nb_comp = nx.number_connected_components(G)

    return {
        "edges": G.number_of_edges(),
        "clustering": nx.average_clustering(G),
        "components": nb_comp,
        "modularity": modularity(G)
    }

# Fonction principale : moyenne des métriques sur plusieurs essais
def moyenne_sur_essais(N=30, n=50, k=3, p=0.05):
    stats_initial = []
    stats_liens = []
    stats_interets = []

    for _ in range(N):
        G0 = nx.relaxed_caveman_graph(n // k, k, 0.05)

        stats_initial.append(get_metrics(G0))

        G1 = reco_link_go(G0.copy())
        stats_liens.append(get_metrics(G1))

        G2 = reco_interests_go(G0.copy())
        stats_interets.append(get_metrics(G2))


    def moyenne(stats):
        return {k: np.mean([d[k] for d in stats]) for k in stats[0]} #pour chaque clé k du premier dictionnaire, 
                                                                    #on prend toutes les valeurs associées à la clé k
                                                                    #et on renvoie leur moyenne 

    return (
        moyenne(stats_initial),
        moyenne(stats_liens),
        moyenne(stats_interets)
    )

def print_metrics(title, stats, color=""):
    header = f"{color} {title}" if color else title
    print(header)
    print(f"   Nombre d'aretes       : {stats['edges']:.1f}")
    print(f"   Clustering coefficient: {stats['clustering']:.3f}")
    print(f"   Composantes connexes  : {stats['components']:.1f}")
    print(f"   Modularity            : {stats['modularity']:.3f}")
    print()


