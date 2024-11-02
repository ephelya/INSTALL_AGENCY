import sqlite3

def drop_tables(cursor):
    tables = ["scenarios", "actions", "scenariosActions", "departments", "agents", "hooks", "projectsHooks", "crons", "projectsCrons", "static_pages"]
    
    for table in tables:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        print(f"Table {table} supprimée si elle existait.")
