#coding:utf8
import networkx as nx
import matplotlib.pyplot as plt

"""
Ce script génère un graphe aléatoire et l'affiche.
"""

def generate_random_graph(n=50, p=0.05):
    """Génère un graphe aléatoirede type voulu."""
    G = nx.erdos_renyi_graph(n=n, p=p)
    return G

def draw_graph(G):
    plt.figure(figsize=(8, 6))
    nx.draw(G, with_labels=False, node_color='lightgrey', edge_color='black')
    plt.title("Graphe Lobster")
    plt.show()

if __name__ == "__main__":
    G = generate_random_graph(25, 0.4)
    draw_graph(G)
