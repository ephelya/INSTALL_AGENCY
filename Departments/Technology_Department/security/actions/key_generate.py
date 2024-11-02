import os
import subprocess

# Importer la fonction d'installation des dépendances
from files.backend.src.services.Technology_Department.devOps.actions.install_dependencies import install_dependencies

# Vérifier si bcrypt est installé, sinon l'installer
try:
    import bcrypt
except ImportError:
    print("bcrypt n'est pas installé. Installation en cours...")
    install_dependencies(['bcrypt'])  # Appel de la fonction pour installer bcrypt
    import bcrypt  # Réessayer l'import après l'installation

def key_generate(login, password):
    """
    Génère un hash sécurisé à partir du login et du mot de passe combinés.

    :param login: Le nom d'utilisateur.
    :param password: Le mot de passe de l'utilisateur.
    :return: Le hash sécurisé (clé) généré.
    """
    combined_input = f"{login}{password}".encode('utf-8')
    salt = bcrypt.gensalt()  # Génère un sel unique
    hashed_key = bcrypt.hashpw(combined_input, salt)  # Hache le login et le mot de passe combinés
    return hashed_key
