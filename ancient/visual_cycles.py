import networkx as nx
import matplotlib.pyplot as plt
from find_cycle_gno import cycle_list
import random


"""
Ce script permet de visualiser les graphes avec des couleurs pour mieux reperer les cycles.
"""

def draw_graph_with_cycles(G, cycles, title="Graphe social avec cycles"):
    plt.figure(figsize=(12, 8))

    pos = nx.spring_layout(G) #positionnement des noeuds 
    
    #graphe du réseau sans cycles
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='lightgray', node_size=700, font_weight='bold')
    plt.pause(3) 

    colors = [ "lightcoral", "lightskyblue", "lightgreen", "plum", "lightsalmon", "lightcyan", "pink",
    "khaki", "thistle", "lavender", "honeydew", "mistyrose", "aliceblue", "lightyellow",
    "palegreen", "peachpuff", "powderblue", "seashell"]

    for i, cycle in enumerate(cycles):
        color = colors[i % len(colors)]
        cycle_edges = [(cycle[j], cycle[(j+1) % len(cycle)]) for j in range(len(cycle))]

        #dessiner les noeuds et arêtes du cycle actuel
        nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='lightgray', node_size=700, font_weight='bold')
        nx.draw_networkx_edges(G, pos, edgelist=cycle_edges, edge_color=color, width=2.5)
        nx.draw_networkx_nodes(G, pos, nodelist=cycle, node_color=color, node_size=800)
        
        plt.pause(1) 

    plt.show()  

if __name__ == "__main__":
    G = load_graph()
    cycles = find_cycles_gno(G)
    print("Nombre de cycles : ", len(cycles))
    draw_graph_with_cycles(G, cycles, "Graphe social initial avec cycles")