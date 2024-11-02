import subprocess
import importlib

def install_dependencies(dependencies, package_manager='pip', cwd=None):
    """
    Installe des dépendances si elles ne sont pas déjà présentes dans l'environnement.

    :param dependencies: Liste de dépendances à installer.
    :param package_manager: Gestionnaire de paquets ('pip' pour Python, 'npm' pour Node.js).
    :param cwd: Répertoire où les dépendances doivent être installées (utile pour npm).
    :return: True si l'installation a réussi, False sinon.
    """
    if not dependencies:
        print("Aucune dépendance à installer.")
        return False

    if package_manager == 'pip':
        for dep in dependencies:
            try:
                importlib.import_module(dep)
                print(f"{dep} est déjà installé.")
            except ImportError:
                print(f"{dep} n'est pas installé. Installation en cours...")
                command = [sys.executable, "-m", "pip", "install", dep]
                subprocess.run(command, check=True, cwd=cwd)
    elif package_manager == 'npm':
        command = f"npm install {' '.join(dependencies)}"
        subprocess.run(command, check=True, shell=True, cwd=cwd)
    else:
        print(f"Gestionnaire de paquets non reconnu : {package_manager}")
        return False

    print(f"Dépendances installées avec succès : {dependencies}")
    return True
