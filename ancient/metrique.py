import networkx as nx
import matplotlib.pyplot as plt

from find_cycle_gno import cycle_list, load_graph
from visual_random import generate_random_graph
from find_cycle_gno import cycle_list



def nb_con_comp(G):
    return nx.number_connected_components(G)

def average_cycle_lenght(G):
    cycles = cycle_list(G)
    if len(cycles) == 0:
        return 0
    else:
        return (sum(len(cycles) for c in cycles) / len(cycles))


def nodes_vs_edges(n=50, p=0.05):
    """Compare le nombre de sommets et d'arêtes dans un graphe aléatoire qui va afficher la courbe 
    représentaive de la loi normale qui est associé."""
    nb_edges = []
    nb_nodes = []
    nb_graphes = 10000
    for _ in range(nb_graphes):
        G = generate_random_graph(n=n, p=p)
        nb_edges.append(G.number_of_edges())
        nb_nodes.append(G.number_of_nodes())


    plt.figure(figsize=(10,6))
    plt.hist(nb_edges, bins=25, alpha=0.5, label='Nombre d\'arêtes')
    plt.ylabel('Nombre d\'arêtes/relations')
    plt.xlabel('Nombre de sommets/personnes')
    plt.grid(True)
    plt.legend()
    plt.title('Distribution du nombre d\'arêtes dans les graphes générés')
    plt.show()


if __name__ == "__main__":
    G = generate_random_graph()  
    print("nb composantes connexes :", nb_con_comp(G))
    print("longueur moyenne des cycles :", average_cycle_lenght(G))
    nodes_vs_edges()
