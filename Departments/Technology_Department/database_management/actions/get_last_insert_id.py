import sqlite3

def get_last_insert_id(table):
    """
    Récupère le dernier ID inséré dans une table donnée.

    :param table: Le nom de la table.
    :return: L'ID du dernier enregistrement inséré.
    """
    conn = sqlite3.connect('agency.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT MAX(id) FROM {table}")
    last_id = cursor.fetchone()[0]

    conn.close()
    return last_id
