import sqlite3

def bdd_get_records_with_join(table, join_table, join_condition, conditions=None, columns=None):
    """
    Récupère les enregistrements d'une table avec une jointure sur une autre table.

    :param table: La table principale à interroger.
    :param join_table: La table avec laquelle effectuer la jointure.
    :param join_condition: La condition de jointure (par ex: 'hooksActions.action_id = actions.id').
    :param conditions: Les conditions pour la requête WHERE (optionnel).
    :param columns: Les colonnes à récupérer (optionnel, par défaut toutes les colonnes).
    :return: Une liste de dictionnaires contenant les enregistrements récupérés.
    """
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    if columns:
        columns_str = ", ".join(columns)
    else:
        columns_str = "*"

    query = f"SELECT {columns_str} FROM {table} JOIN {join_table} ON {join_condition}"

    if conditions:
        condition_str = " AND ".join([f"{key} = ?" for key in conditions.keys()])
        query += f" WHERE {condition_str}"

    cursor.execute(query, tuple(conditions.values()) if conditions else ())
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(dict(zip([col[0] for col in cursor.description], row)))

    cursor.close()
    conn.close()
    return result
