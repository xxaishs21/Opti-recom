import networkx as nx

def cycle_list(G):
    """Trouve tous les cycles dans un graphe orienté."""
    return list(nx.simple_cycles(G))  # Utilisation de la fonction intégrée de NetworkX
