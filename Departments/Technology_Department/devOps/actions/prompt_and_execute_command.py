import subprocess

def prompt_and_execute_command(command, working_directory=None):
    """Demande une confirmation avant d'exécuter une commande dans un répertoire donné."""
    confirmation = input(f"Voulez-vous exécuter la commande '{command}' dans le répertoire '{working_directory}' ? (Y/n) ").strip().lower()
    
    if confirmation in ['y', 'yes', '']:
        try:
            subprocess.run(command, shell=True, cwd=working_directory)
            print(f"Commande '{command}' exécutée avec succès.")
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de la commande : {e}")
    else:
        print(f"Commande '{command}' annulée par l'utilisateur.")

