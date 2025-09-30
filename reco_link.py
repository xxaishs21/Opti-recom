from copy import deepcopy
import networkx as nx

def reco_link_gno(G, seuil=1):
    """
    Recommande des liens à partir des amis communs.
    Si deux nœuds ont au moins `seuil` amis communs, on ajoute une arête entre eux.
    """
    G2 = deepcopy(G)  #on travaille sur une copie pour comparer visuellement avant et apres
    nodes = list(G.nodes)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]

            if not G2.has_edge(u, v):
                amis_u = set(G.neighbors(u))
                amis_v = set(G.neighbors(v))
                amis_communs = amis_u & amis_v

                if len(amis_communs) >= seuil:
                    G2.add_edge([u], [v])

    return G2

#____________________________________________________________________________________________________________________

def reco_link_go(G, seuil=1):
    """
    Recommande des liens à partir des amis communs.
    Si deux nœuds ont au moins `seuil` amis communs, on ajoute une arête entre eux.
    """
    G2 = deepcopy(G)  #on travaille sur une copie pour comparer visuellement avant et apres
    nodes = list(G.nodes)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]
            
            ensU = set(G2.edges(u))
            
            if not v in ensU :
                amis_u = set(G.neighbors(u))
                amis_v = set(G.neighbors(v))
                amis_communs = amis_u & amis_v

                if len(amis_communs) >= seuil:
                    G2.add_edge(u, v)
                    G2.add_edge(v, u)

    return G2

#G0 = nx.random_partition_graph([3]*3, 0.3, 0.25)
#print(reco_link_go(G0))