import networkx as nx
import networkx.algorithms.community as nx_comm
from copy import deepcopy

from reco_link import reco_link_go
from find_cycle_go import cycle_list
from reco_interest import reco_interests_go


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

        G1 = reco_link_go(deepcopy(G0))
        stats_liens.append(get_metrics(G1))

        G2 = reco_interests_go(deepcopy(G0))
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


