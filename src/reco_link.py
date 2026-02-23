from copy import deepcopy
import networkx as nx
import random

def reco_link_gno(G, seuil=1):
    """
    Recommande des liens à partir des amis communs (version probabiliste).
    Si deux nœuds ont au moins `seuil` amis communs, on ajoute une arête
    avec une probabilité croissante en fonction du nombre d'amis communs.
    """
    G2 = G.copy() 
    nodes = list(G.nodes)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]

            if not G2.has_edge(u, v):
                amis_u = set(G.neighbors(u))
                amis_v = set(G.neighbors(v))
                amis_communs = amis_u & amis_v
                nb = len(amis_communs)

                if nb >= seuil:
                    p = 1 - (seuil / (nb + 1))
                    if random.random() < p:
                        G2.add_edge(u, v)

    return G2


#____________________________________________________________________________________________________________________

def reco_link_go(G, seuil=1):
    """
    Recommande des liens à partir des amis communs (version probabiliste).
    Si deux nœuds ont au moins `seuil` amis communs, on ajoute une arête
    (dans les deux sens) avec une probabilité croissante en fonction du
    nombre d'amis communs.
    """
    G2 = G.copy()  
    nodes = list(G.nodes)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            
            ensU = set(G2.edges(u))
            
            if not v in ensU:
                amis_u = set(G.neighbors(u))
                amis_v = set(G.neighbors(v))
                amis_communs = amis_u & amis_v
                nb = len(amis_communs)

                if nb >= seuil:
                    p = 1 - (seuil / (nb + 1))
                    if random.random() < p:
                        G2.add_edge(u, v)
                        G2.add_edge(v, u)

    return G2
