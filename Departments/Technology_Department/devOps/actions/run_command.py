import os
import subprocess


def run_command(command, cwd=None):
    try:
        subprocess.run(command, check=True, shell=True, cwd=cwd)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")
        return False
