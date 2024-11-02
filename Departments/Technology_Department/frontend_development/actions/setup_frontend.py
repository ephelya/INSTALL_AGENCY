import os
from files.backend.src.services.Technology_Department.architecture.actions.create_directory import create_directory
from files.backend.src.services.Technology_Department.frontend_development.actions.create_react_file import create_react_file
from files.backend.src.services.Technology_Department.devOps.actions.update_package_json import update_package_json
from files.backend.src.services.Technology_Department.devOps.actions.install_dependencies import install_dependencies 

def setup_frontend(frontend_path):
    # Création des répertoires supplémentaires
    additional_directories = [
        "src/templates/partials",
        "src/templates/sections",
        "src/services",
        "src/pages",
        "src/components",
        "build/static/css/apis",
    ]
    
    # Passer à chaque répertoire à créer le chemin source et la destination
    for directory in additional_directories:
        create_directory(directory, frontend_path)  # Ajout du chemin source (directory) et de la destination (frontend_path)

    # Création des fichiers React
    create_react_file(frontend_path)

    # Mise à jour du package.json
    update_package_json(frontend_path)

    # Installation des dépendances
    dependencies = ['react-router-dom', 'react', 'react-dom']  # Ajoutez d'autres dépendances si nécessaire
    install_dependencies(dependencies, package_manager='npm', cwd=frontend_path)
