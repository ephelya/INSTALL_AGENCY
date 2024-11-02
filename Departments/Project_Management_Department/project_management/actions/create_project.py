import os 
from files.backend.src.services.Technology_Department.database_management.actions.database_setup  import database_setup
from files.backend.src.services.Technology_Department.architecture.actions.create_directory import create_directory
from files.backend.src.services.Technology_Department.architecture.actions.copy_directory import copy_directory
from files.backend.src.services.Technology_Department.frontend_development.actions.create_react_app import create_react_app
from files.backend.src.services.Technology_Department.frontend_development.actions.setup_frontend import setup_frontend
from files.backend.src.services.Technology_Department.backend_development.actions.setup_backend import setup_backend
from files.backend.src.services.Technology_Department.devOps.actions.run_command import run_command
from files.backend.src.services.Technology_Department.devOps.actions.prompt_and_execute_command import prompt_and_execute_command
from files.backend.src.services.Technology_Department.frontend_development.actions.create_main_files import create_main_files
# Constantes
INSTALL_PATH = "/Users/nathalie/Dropbox/PROJETS/INSTALL/files/backend/src"

# Exécuter le script de création de la base de données avant le reste du processus
database_setup("/Users/nathalie/Dropbox/PROJETS/INSTALL/database.py")

def create_project(db_install_path, db_install_file):
    project_name = input("Veuillez entrer le nom du projet à créer : ")
    project_path = os.path.expanduser(f"~/Dropbox/PROJETS/{project_name}")
    frontend_path = os.path.join(project_path, "frontend")
    backend_path = os.path.join(project_path, "backend")

    print(f"Création du projet : {project_path}")

    # Configuration de la base de données
    database_setup(db_install_file)
    # Création des répertoires principaux
    create_directory(project_name, os.path.expanduser("~/Dropbox/PROJETS"))  # Création du répertoire principal du projet
    create_directory("frontend", project_path)  # Création du répertoire frontend
    create_directory("backend", project_path)   # Création du répertoire backend



    # Copie de la structure des services
    files_src_path = os.path.join(INSTALL_PATH)  # Utiliser INSTALL_PATH directement
    files_dest_path = os.path.join(backend_path, "src")
    print(f"install : {INSTALL_PATH} on copie {files_src_path} vers {files_dest_path}")

    copy_directory(files_src_path, files_dest_path)


    # Configuration du frontend
    if create_react_app(project_path):
        setup_frontend(frontend_path)

        # Build du projet React
        print("Génération du build React...")
        if run_command("npm run build", cwd=frontend_path):
            print("Build React généré avec succès")
        else:
            print("Erreur lors de la génération du build React")
    
    # Configuration du backend
    setup_backend(backend_path, project_name)

    print(f"Le projet a été créé avec succès à l'emplacement : {project_path}")
    # Pour le backend
    prompt_and_execute_command("npm start", backend_path)

    # Pour le frontend
    prompt_and_execute_command("npm start", frontend_path)
