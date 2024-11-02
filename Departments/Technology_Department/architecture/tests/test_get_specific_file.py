import os

def get_specific_file(directory, file_name):
    """
    Recherche récursive d'un fichier spécifique dans un répertoire et ses sous-répertoires.

    :param directory: Chemin vers le répertoire de base dans lequel chercher le fichier
    :param file_name: Nom du fichier à rechercher
    :return: Chemin complet du fichier si trouvé, sinon None
    """
    try:
        # Parcours récursif des sous-répertoires
        for root, dirs, files in os.walk(directory):
            if file_name in files:
                return os.path.join(root, file_name)
        print(f"Le fichier {file_name} est introuvable dans {directory} et ses sous-répertoires.")
        return None
    except Exception as e:
        print(f"Une erreur est survenue : {e}")
        return None
