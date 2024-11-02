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

def check_key(login, password, stored_key):
    """
    Vérifie si le hash du login et du mot de passe correspond à la clé stockée.

    :param login: Le nom d'utilisateur.
    :param password: Le mot de passe de l'utilisateur.
    :param stored_key: Le hash sécurisé stocké.
    :return: True si la clé correspond, sinon False.
    """
    combined_input = f"{login}{password}".encode('utf-8')
    return bcrypt.checkpw(combined_input, stored_key)  # Vérifie si les informations correspondent
