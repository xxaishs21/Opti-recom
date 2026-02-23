import sqlite3

def get_db_connection():
    """Renvoie une connexion à la base de données SQLite."""
    return sqlite3.connect("C:\\Users\\sania\\OneDrive\\Desktop\\TIPE\\social-network.db")
