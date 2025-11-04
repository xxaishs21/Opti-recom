import networkx as nx
import networkx as nx

# ------------------- POUR UN GRAPHE NON ORIENTE -------------------

def cycle_list_gno(G):
    """Renvoie la liste de tous les cycles d’un graphe non orienté.

    Args:
        G (networkx.Graph): Graphe non orienté.

    Returns:
        list[list]: Liste de tous les cycles simples de G.
    """
    return nx.cycle_basis(G)


# ------------------- POUR UN GRAPHE ORIENTE -------------------

def cycle_list_go(G):
    """Trouve tous les cycles dans un graphe orienté."""
    return list(nx.simple_cycles(G))  # Utilisation de la fonction intégrée de NetworkX

"""
G0 = nx.random_partition_graph([3]*3, 0.3, 0.25)
cycles = cycle_list(G0)
print(f"Nombre de cycles trouve dans le graphe oriente) : {len(cycles)}")
print(cycles)  
"""