import subprocess

def github_update(commit_message="Mise à jour automatique de l'agence"):
    """
    Vérifie les modifications, les ajoute, les commite et les pousse vers le dépôt distant.
    """
    try:
        # Vérifie s'il y a des modifications à pousser
        status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
        
        # S'il y a des modifications, les ajoute, commite et pousse
        if status.stdout:
            subprocess.run(["git", "add", "."], check=True)
            subprocess.run(["git", "commit", "-m", commit_message], check=True)
            subprocess.run(["git", "push", "-u", "origin", "main"], check=True)
            print("Modifications poussées vers GitHub avec succès.")
        else:
            print("Aucune modification détectée.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la mise à jour du dépôt GitHub : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    github_update()
