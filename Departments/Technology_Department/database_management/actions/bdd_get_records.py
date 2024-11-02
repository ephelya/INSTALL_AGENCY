import sqlite3

def bdd_get_records(table, conditions=None, columns=None):
    """
    Récupère des enregistrements d'une table en fonction des conditions spécifiées.

    :param table: Le nom de la table où récupérer les données
    :param conditions: Un dictionnaire des colonnes et valeurs pour filtrer les résultats (facultatif)
    :param columns: Une liste des colonnes à récupérer (facultatif, par défaut toutes les colonnes)
    :return: Une liste de dictionnaires représentant les enregistrements ou un enregistrement unique
    """
    conn = sqlite3.connect('agency.db')
    cursor = conn.cursor()

    # Colonnes à récupérer
    if columns:
        columns_str = ', '.join(columns)
    else:
        columns_str = '*'

    # Construction de la clause WHERE
    where_clause = ''
    if conditions:
        where_clause = ' WHERE ' + ' AND '.join([f"{col} = ?" for col in conditions.keys()])
    
    # Requête SQL
    query = f"SELECT {columns_str} FROM {table}{where_clause}"

    # Exécution de la requête
    cursor.execute(query, tuple(conditions.values()) if conditions else ())

    # Récupérer tous les résultats
    rows = cursor.fetchall()
    columns_names = [desc[0] for desc in cursor.description]

    # Convertir les résultats en une liste de dictionnaires
    records = [dict(zip(columns_names, row)) for row in rows]

    conn.close()

    # Si un seul enregistrement est trouvé, le renvoyer directement
    if len(records) == 1:
        return records[0]
    
    return records
