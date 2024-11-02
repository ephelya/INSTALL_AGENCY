import os

def get_directories(path):
    """
    Retourne la liste des sous-répertoires dans un chemin donné.

    :param path: Chemin du répertoire parent
    :return: Liste des sous-répertoires
    """
    try:
        directories = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
        return directories
    except FileNotFoundError:
        print(f"Le chemin spécifié {path} n'existe pas.")
        return []
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return []
