import sqlite3
def bddUpdateRecords(table, update_data, conditions):
    """
    Met à jour des enregistrements dans une table de la base de données.

    :param table: Le nom de la table où mettre à jour les données
    :param update_data: Un dictionnaire des colonnes à mettre à jour et leurs nouvelles valeurs
    :param conditions: Un dictionnaire des conditions (colonnes et valeurs) pour filtrer les enregistrements à mettre à jour
    """
    conn = sqlite3.connect('agency.db')
    cursor = conn.cursor()

    # Construction des clauses SET et WHERE pour la requête SQL
    set_clause = ', '.join([f"{col} = ?" for col in update_data.keys()])
    where_clause = ' AND '.join([f"{col} = ?" for col in conditions.keys()])

    query = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

    # Exécuter la requête de mise à jour
    try:
        cursor.execute(query, list(update_data.values()) + list(conditions.values()))
        conn.commit()
        print(f"Enregistrements mis à jour dans {table}")
    except sqlite3.Error as e:
        print(f"Erreur lors de la mise à jour dans {table}: {e}")
    finally:
        conn.close()
