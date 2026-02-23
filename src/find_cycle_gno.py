
def dfs(G, path, visited_nodes):
    """
    Parcours en profondeur le graphe G.
    
    Args : 
        G (_Networkx_) : graphe social où les sommets représentent les personnes
        path (_list_) : chemin parcouru (à mettre contenant uniquement le premier élément)
        visited_nodes (_set_) : noeuds visités dans le parcours (contenant initialement uniquement le premier élément) 
    
    Returns : 
        _list_ : tous les cycles à partir du noeud donnée dans path
    """
    node = path[-1]
    cycles = []
    visited_edges = set()
    
    for neighbor in G[node]:
        edge = (node, neighbor)
        
        if edge in visited_edges:
            
            if neighbor in path:
                
                if len(path) < 2 or neighbor != path[-2]: #vérifie que c'est pas une arete 
                    idx = path.index(neighbor)
                    cycle = path[idx:] #prend la liste des noeuds en enlevant le doublon
                    
                    if set(cycle) not in [set(c) for c in cycles]: #verifie que le cycle n'est pas deja vu 
                        cycles.append(cycle)
            
            elif neighbor not in visited_nodes:
                visited_edges.add(edge)
                dfs(G, path + [neighbor], visited_nodes | {neighbor})
    
    return cycles

#Compléxité dfs(...) : O(|S|^2)
#   - une boucle for en nombre de sommets présent dans le graphe -> O(|S|) avec S l'ensemble de sommets
#   - fonction récursive en nombre de sommets présent dans le graphe -> O(|S|)      //

def cycle_list(G):
    """
    Liste tous les cycles dans le graphe donné en paramètres.

    Args:
        G (_Networkx_): graphe social où les sommets représentent les personnes

    Returns:
        _type_: liste de tous les cycles présent dans le graphe à partir de n'importe quel noeud.
    """
    lst_cycles = []

    for start_node in G.nodes:
        lst_cycles.append(dfs(G, [start_node], {start_node}))

    return lst_cycles

#Compléxité cycle_list(...) : O(|S|^3)
#   - on applique le parcours de graphe à chaqu'un des sommets pour avoir la liste de tous les cycles 
