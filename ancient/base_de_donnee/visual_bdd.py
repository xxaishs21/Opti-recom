#coding:utf8
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from bdd import get_db_connection  

"""
Ce script génère une visualisation du graphe social à partir de la base de données.
"""

def load():
    """Charge les données de la base et les transforme en DataFrame."""
    connexion = get_db_connection()
    
    fr_query = """
    SELECT 
        Friendships.user_id AS user_id, 
        Friendships.friend_id AS friend_id
    FROM Friendships
    """
    friendships_df = pd.read_sql(fr_query, connexion)

    users_query = "SELECT id, name FROM User"
    users_df = pd.read_sql(users_query, connexion)

    connexion.close()  # Fermer la connexion après récupération des données

    # Mapper les IDs en noms d'utilisateur
    id_to_name = dict(zip(users_df["id"], users_df["name"]))
    friendships_df["user_id"] = friendships_df["user_id"].map(id_to_name)
    friendships_df["friend_id"] = friendships_df["friend_id"].map(id_to_name)

    return friendships_df

def draw(df, s, t):
    """Affiche le graphe du réseau social."""
    G = nx.from_pandas_edgelist(df, source=s, target=t)

    plt.figure(figsize=(12,8))
    nx.draw(G, with_labels=True, node_color='skyblue', node_size=700, edge_color='red', font_weight='bold')
    plt.show()

if __name__ == "__main__":
    df = load()
    draw(df, "user_id", "friend_id")
