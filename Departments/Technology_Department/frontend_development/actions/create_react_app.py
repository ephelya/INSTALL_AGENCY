import os
from files.backend.src.services.Technology_Department.devOps.actions.run_command import run_command

def create_react_app(project_path):
    if run_command(f"npx create-react-app frontend", cwd=project_path):
        print(f"Projet React créé avec succès : {os.path.join(project_path, 'frontend')}")
        return True
    else:
        print("Erreur lors de la création du projet React")
        return False

