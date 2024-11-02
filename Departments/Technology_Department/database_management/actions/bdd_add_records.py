import sqlite3
def bddAddRecords(table, datas):
    """
    Ajoute des enregistrements dans une table de la base de données.

    :param table: Le nom de la table où insérer les données.
    :param datas: Un tableau de tuples contenant les colonnes et les valeurs à insérer.
    """
    conn = sqlite3.connect('agency.db')  # Chemin vers la base de données
    cursor = conn.cursor()

    try:
        # Générer la requête d'insertion en fonction du nombre de colonnes
        columns = ', '.join([col for col, _ in datas])
        placeholders = ', '.join(['?' for _ in datas])
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        
        # Préparer les valeurs
        values = [val for _, val in datas]

        # Exécuter la requête d'insertion
        cursor.execute(query, values)
        conn.commit()
        print(f"Enregistrement ajouté avec succès dans {table}")
    except sqlite3.Error as e:
        print(f"Erreur lors de l'ajout dans {table}: {e}")
    finally:
        conn.close()

