import os
import subprocess
from files.backend.src.services.Technology_Department.devOps.actions.install_dependencies import install_dependencies  # Importer la fonction générique

# Vérifier si cryptography.fernet est installé, sinon l'installer
try:
    from cryptography.fernet import Fernet
except ImportError:
    print("cryptography.fernet n'est pas installé. Installation en cours...")
    install_dependencies(['cryptography'])  # Installation de cryptography si absent
    from cryptography.fernet import Fernet  # Réessayer l'import après installation

def generate_encryption_key(key_path="encryption_key.key"):
    """
    Génère ou récupère une clé de chiffrement Fernet.
    
    :param key_path: Le chemin du fichier où la clé sera sauvegardée ou récupérée.
    :return: La clé de chiffrement.
    """
    if not os.path.exists(key_path):
        # Générer une clé de chiffrement (à faire une seule fois)
        encryption_key = Fernet.generate_key()
        # Sauvegarder la clé de chiffrement
        with open(key_path, "wb") as key_file:
            key_file.write(encryption_key)
    else:
        # Charger la clé de chiffrement existante
        with open(key_path, "rb") as key_file:
            encryption_key = key_file.read()

    return encryption_key
