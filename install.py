import os
import shutil
import subprocess
from core.github_update import github_update  # Import de la fonction pour la mise à jour GitHub

def setup_directories():
    project_dir = os.getcwd()
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/logs"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/logs"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/models"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/tests"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/logs"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/models"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "Documentation/rules"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Documentation/scripts"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Documentation/templates"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Templates"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "core"), exist_ok=True)
    print("Structure de répertoires créée.")

def set_executable_permissions():
    deploy_script_path = os.path.join("core", "deploy_to_github.sh")
    if os.path.exists(deploy_script_path):
        os.chmod(deploy_script_path, 0o755)
        print(f"Permissions d'exécution ajoutées pour {deploy_script_path}.")

def copy_agent_file():
    source_path = os.path.join("core", "AIAgent.py")
    destination_path = os.path.join("Departments", "AI_Department", "AIAgent.py")
    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
        print(f"AIAgent.py copié vers {destination_path}.")
    else:
        print("AIAgent.py est introuvable dans le répertoire 'core'.")

def initialize_agency():
    from Departments.AI_Department.AIAgent import AIAgent
    
    agent = AIAgent()
    agent.create_function(
        department="General_Direction",
        function_name="supervise_agents",
        services_path="services",
        metadatas="# Metadata: version=1.0, author='General_Direction'",
        imports="import os",
        inputs="agent_list",
        description="Supervise la liste des agents.",
        body="# Code de supervision des agents"
    )
    print("Fonction supervise_agents créée dans General_Direction.")

if __name__ == "__main__":
    setup_directories()
    set_executable_permissions()
    copy_agent_file()
    initialize_agency()
    
    # Mise à jour du dépôt sur GitHub
    github_update(commit_message="Mise à jour post-installation")
    print("Installation et mise à jour du dépôt GitHub terminées.")
