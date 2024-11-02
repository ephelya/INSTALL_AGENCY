import os

def create_env_file(db_name, db_user, db_password, db_host="localhost", db_port="5432"):
    """
    Crée un fichier .env avec les informations de connexion à la base de données.

    Args:
        db_name (str): Nom de la base de données.
        db_user (str): Nom d'utilisateur de la base de données.
        db_password (str): Mot de passe de l'utilisateur de la base de données.
        db_host (str, optional): Hôte de la base de données. Par défaut "localhost".
        db_port (str, optional): Port de la base de données. Par défaut "5432".
    """
    env_content = f"""DB_NAME={db_name}
DB_USER={db_user}
DB_PASSWORD={db_password}
DB_HOST={db_host}
DB_PORT={db_port}
"""
    with open(".env", "w") as env_file:
        env_file.write(env_content)
    
    print(".env file created with database configuration.")
