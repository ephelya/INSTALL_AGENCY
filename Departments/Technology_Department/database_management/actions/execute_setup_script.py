import os
import subprocess  # Utilisation du module intégré Python

def execute_setup_script(script_path):
    """
    Exécute un script donné pour effectuer une installation ou une configuration.
    Le chemin complet du script doit être fourni en paramètre.
    """
    if os.path.exists(script_path):
        try:
            subprocess.run(f"python3 {script_path}", check=True, shell=True)  # Exécution du script
            print(f"{os.path.basename(script_path)} exécuté avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de {script_path} : {e}")
    else:
        print(f"Le fichier {script_path} n'existe pas.")
