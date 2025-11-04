import random
import math
from copy import deepcopy
import networkx as nx
from find_cycle import cycle_list_go

center_interest = {0 : 'dessin',
                    1 : 'musique',
                    2: 'sport',
                    3 : 'lecture',
                    4 : 'voyage',
                    5 : 'cinéma',
                    6 : 'jeux vidéo',
                    7 : 'cuisine',
                    8 : 'animaux',
                    9 : 'mode',
                    10 : 'technologie',
                    11 : 'politique',
                    12 : 'art'}

def solo_likes (user1 : list):
    """Créee de maniere aléatoire un vecteur 'user' qui caractérise ses centres d'intérets avec 0 ou 1." 
    Args:
        user1 (list): liste vide 
    Returns:
        list: liste des centre d'intérets contenant 0 ou 1.
    """
    for i in range (len(user1)) :
        user1[i] = random.randint(0, 1)
    return user1

#user1 = [0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0]
#user2 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#user3 = [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0]

user1 = [0] * 12
user2 = [0] * 12
user3 = [0] * 12
user1 = solo_likes(user1)
user2 = solo_likes(user2)
user3 = solo_likes(user3)

def interest(user1 : list, user2 : list):
    """Regarde les intérets communs des deux utilisateurs.
    Args:
        user1 (list): centres d'intérets de user1
        user2 (list): centres d'intérets de user2
    Returns:
        list: liste contenant des 0 ou des 1 qui represente si ce theme est apprécié par les deux utilisateurs ou non."
    """
    inter_list = [0] * len(user1) 
    for i in range (len(user1) - 1) : 
        if user1[i] == user2[i] : 
            inter_list[i] = 1
    return inter_list

def cosine_similarity(a, b):
    """Calcule la similarité cosinus entre deux vecteurs numériques.
    Args:
        a (list[float]): Premier vecteur, représenté par une liste (ou séquence) de nombres.
        b (list[float]): Deuxième vecteur, représenté par une liste (ou séquence) de nombres.
    Returns:
        float: Similarité cosinus entre a et b, égale à 0.0 si l’un des deux vecteurs est nul.
    """

    def dot_product(a, b):
        return sum(x * y for x, y in zip(a, b))

    def norm(v):
        return math.sqrt(sum(x * x for x in v))
    
    na = norm(a)
    nb = norm(b)
    if na == 0 or nb == 0:
        return 0.0  # Similarité nulle si l’un des deux est nul
    return dot_product(a, b) / (na * nb)

def can_reco(user1, user2) : 
    if cosine_similarity(user1, user2) >= 0.65 : 
        return True 
    else : 
        return False 

# ------------------- POUR UN GRAPHE NON ORIENTE -------------------

def reco_interests_gno(G, seuil=0.65, d=12):
    """
    Recommande des liens à partir de la similarité des intérêts entre utilisateurs.    
    Args: 
        G : graphe de type Networkx - non orienté 
        seuil : à partir duquel on va considérer qu'une connection doit avoir lieu
        d : longueur de la liste du vecteur d'intéret.
    Returns: 
        Networkx graph : graphe modifié après avoir appliqué la recommandation par intérets.  
    """
    G2 = G.copy()
    vecteurs = {}  # dictionnaire : noeud -> vecteur d'intérêt

    for node in G2.nodes:
        vecteurs[node] = solo_likes([0] * d)

    nodes = list(G2.nodes)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]

            if not G2.has_edge(u, v):
                sim = cosine_similarity(vecteurs[u], vecteurs[v])
                if sim >= seuil:
                    G2.add_edge(u, v)

    return G2

# ------------------- POUR UN GRAPHE ORIENTE -------------------

def reco_interests_go(G, seuil=0.65, d=12):
    """
    Recommande des liens à partir de la similarité des intérêts entre utilisateurs.    
    Args: 
        G : graphe de type Networkx - orienté 
        seuil : à partir duquel on va considérer qu'une connection doit avoir lieu
        d : longueur de la liste du vecteur d'intéret.
    Returns: 
        Networkx graph : graphe modifié après avoir appliqué la recommandation par intérets.  
    """
    G2 = G.copy()
    vecteurs = {}  # dictionnaire : noeud -> vecteur d'intérêt

    for node in G2.nodes:
        vecteurs[node] = solo_likes([0] * d)

    nodes = list(G2.nodes)

    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            u, v = nodes[i], nodes[j]

            if not G2.has_edge(u, v) :
                sim = cosine_similarity(vecteurs[u], vecteurs[v])
                if sim >= seuil:
                    G2.add_edge(u, v)

    return G2






