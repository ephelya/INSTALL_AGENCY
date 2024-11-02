import os

def create_directory(directory, destination_directory):
    """
    Crée un répertoire à l'emplacement spécifié.

    Args:
        directory (str): Le nom du répertoire à créer.
        destination_directory (str): Le chemin du répertoire parent où le répertoire sera créé.
    """
    full_path = os.path.join(destination_directory, directory)

    try:
        # Créer le répertoire complet
        os.makedirs(full_path, exist_ok=True)
        print(f"Répertoire créé ou déjà existant : {full_path}")

    except Exception as e:
        print(f"Erreur lors de la création du répertoire {full_path} : {e}")
