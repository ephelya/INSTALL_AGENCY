import os
import subprocess
import sys
import shutil
from dotenv import load_dotenv
from core.github_update import github_update  # Fonction pour la mise à jour GitHub

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

def create_env_file(db_name="my_database", db_user="my_user", db_password="my_password", db_host="localhost", db_port="5432"):
    """
    Crée un fichier .env avec les informations de connexion à la base de données.
    """
    env_content = f"""DB_NAME={db_name}
DB_USER={db_user}
DB_PASSWORD={db_password}
DB_HOST={db_host}
DB_PORT={db_port}
"""
    with open(".env", "w") as env_file:
        env_file.write(env_content)
    
    print(".env file created with database configuration.")

def setup_local_database():
    """
    Configure la base de données locale en utilisant les paramètres du fichier .env.
    """
    # Importer psycopg2-binary seulement après son installation
    import psycopg2
    from psycopg2 import sql

    # Charger les paramètres depuis le fichier .env
    load_dotenv()
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST", "localhost")
    db_port = os.getenv("DB_PORT", "5432")

    try:
        # Connexion à PostgreSQL
        conn = psycopg2.connect(
            dbname="postgres",
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        conn.autocommit = True
        cursor = conn.cursor()

        # Création de la base de données si elle n'existe pas
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(db_name)))
        print(f"Base de données '{db_name}' créée avec succès.")
        cursor.close()
        conn.close()

    except psycopg2.OperationalError as e:
        print(f"Erreur de connexion à la base de données : {e}")
    except psycopg2.errors.DuplicateDatabase:
        print(f"La base de données '{db_name}' existe déjà.")
    except Exception as e:
        print(f"Erreur lors de la création de la base de données : {e}")

def setup_directories():
    project_dir = os.getcwd()
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/logs"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/General_Direction/tests"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/logs"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/models"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/AI_Department/tests"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/logs"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/models"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Technology_Department/tests"), exist_ok=True)

    os.makedirs(os.path.join(project_dir, "Departments/Project_Management_Department/actions"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Project_Management_Department/resources"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Project_Management_Department/logs"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Project_Management_Department/models"), exist_ok=True)
    os.makedirs(os.path.join(project_dir, "Departments/Project_Management_Department/tests"), exist_ok=True)

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
    # Ajouter le chemin "Departments" au sys.path pour garantir que les modules puissent être importés
    sys.path.append(os.path.join(os.getcwd(), "Departments"))
    try:
        from AI_Department.AIAgent import AIAgent
        agent = AIAgent()
        agent.create_function(
            department="General_Direction",
            function_name="supervise_agents",
            services_path="Departments",
            file_type="action",
            author="General_Direction",
            file_version="1.0",
            file_mission="Supervise la liste des agents",
            imports=["os"],
            inputs_params=["agent_list"],
            output_params=["status"],
            description="Supervise la liste des agents et renvoie leur statut.",
            body="# Code de supervision des agents"
        )
        print("Fonction supervise_agents créée dans General_Direction.")
    except ImportError as e:
        print(f"Erreur d'importation : {e}")
    except Exception as ex:
        print(f"Erreur lors de l'initialisation de l'agence : {ex}")

if __name__ == "__main__":
    # Installation générique des packages
    packages_to_install = ["psycopg2-binary", "python-dotenv"]
    install_required_packages(packages_to_install)

    # Configuration des répertoires et permissions
    setup_directories()
    set_executable_permissions()
    copy_agent_file()
    initialize_agency()
    
    # Création du fichier .env et configuration de la base de données
    create_env_file()            
    setup_local_database()

    # Mise à jour du dépôt sur GitHub
    github_update(commit_message="Mise à jour post-installation")
    print("Installation et mise à jour du dépôt GitHub terminées.")
