import networkx as nx

def cycle_list(G):
    """Trouve tous les cycles dans un graphe orienté."""
    return list(nx.simple_cycles(G))  # Utilisation de la fonction intégrée de NetworkX


"""
G0 = nx.random_partition_graph([3]*3, 0.3, 0.25)
cycles = cycle_list(G0)
print(f"Nombre de cycles trouve dans le graphe oriente) : {len(cycles)}")
print(cycles)  
"""