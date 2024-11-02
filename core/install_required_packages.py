import subprocess
import sys

def install_required_packages(packages):
    """
    Installe les packages spécifiés, en vérifiant d'abord s'ils sont déjà installés.

    Args:
        packages (list): Liste de noms de packages à installer.
    """
    for package in packages:
        try:
            # Vérifie si le package est déjà installé
            __import__(package)
            print(f"{package} est déjà installé.")
        except ImportError:
            # Installe le package s'il n'est pas installé
            print(f"Installation de {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Exemple d'utilisation
if __name__ == "__main__":
    packages_to_install = ["psycopg2", "dotenv"]  # Liste des packages requis
    install_required_packages(packages_to_install)
