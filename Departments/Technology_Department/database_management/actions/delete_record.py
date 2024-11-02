import sqlite3

def delete_record(table, conditions):
    """
    Supprime un enregistrement dans une table en fonction des conditions spécifiées.

    :param table: Le nom de la table où supprimer les données
    :param conditions: Un dictionnaire des colonnes et valeurs à utiliser comme filtre
    """
    conn = sqlite3.connect('agency.db')
    cursor = conn.cursor()

    # Construction de la clause WHERE pour la requête SQL
    where_clause = ' AND '.join([f"{col} = ?" for col in conditions.keys()])

    query = f"DELETE FROM {table} WHERE {where_clause}"

    # Exécuter la requête de suppression
    try:
        cursor.execute(query, list(conditions.values()))
        conn.commit()
        print(f"Enregistrements supprimés de {table}")
    except sqlite3.Error as e:
        print(f"Erreur lors de la suppression dans {table}: {e}")
    finally:
        conn.close()
