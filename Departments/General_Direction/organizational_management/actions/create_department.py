import os
from backend.src.services.Technology_Department.architecture import create_directory, create_file
from backend.src.services.Technology_Department.database_management import bdd_add_records, get_last_insert_id
from backend.src.services.Technology_Department.automation import hook

def create_department(department):
    """
    Crée un nouveau département, son répertoire, ses tables associées, et définit les services et agents.
    Un hook after_create_department est déclenché à la fin de la création.
    :param department: Nom du département à créer
    """
    
    base_path = f"./{department}"
    
    # 1. Créer le fichier department_overview.txt et déployer le répertoire avec ses sous-dossiers
    overview_file = os.path.join(base_path, "department_overview.txt")
    directories = ["actions", "models", "resources/docs", "resources/guides", "resources/medias", "tests"]
    
    # Utilisation des fonctions génériques pour créer le répertoire et les fichiers
    create_directory(base_path)
    for dir_name in directories:
        create_directory(os.path.join(base_path, dir_name))
    
    # Création du fichier department_overview.txt avec une structure initiale
    overview_content = f"Department: {department}\nRole: \nServices: \n"
    create_file(overview_file, overview_content)

    # 2. Créer la table du département dans la BDD
    department_data = [
        ("name", department),
        ("role", "")
    ]
    bdd_add_records("departments", department_data)
    department_id = get_last_insert_id("departments")

    # 3. Définir les services du département et les ajouter à la BDD
    services = ["Service A", "Service B", "Service C"]  # Exemple de services, cela peut être dynamique
    for service in services:
        service_data = [
            ("departmentId", department_id),
            ("service", service),
            ("role", f"Role for {service}")
        ]
        bdd_add_records("departmentsServices", service_data)
    
    # 4. Définir les caractéristiques de l'agent du département et créer le fichier <department>_manager_agent.py
    agent_name = f"{department}_manager_agent.py"
    agent_content = f"""
from backend.src.services.General_Direction.abstract_manager_agent import AbstractManagerAgent

class {department.capitalize()}ManagerAgent(AbstractManagerAgent):
    def manage(self):
        print("Gère le département {department}")

    def report(self):
        print("Rapport du département {department}")
    """
    
    create_file(os.path.join(base_path, agent_name), agent_content)
    
    # Ajouter l'agent dans la BDD
    agent_data = [
        ("departmentId", department_id),
        ("serviceId", None),  # NULL pour les managers
        ("role", "Manager"),
        ("name", f"{department.capitalize()} Manager"),
        ("dateCreation", "datetime('now')")
    ]
    bdd_add_records("agents", agent_data)
    agent_id = get_last_insert_id("agents")

    # 5. Demander à l'agent manager de définir les caractéristiques, droits et rôles des agents des différents services
    agent_params = [
        ("Leadership", "Capacité de gestion des équipes"),
        ("Strategy", "Définition des orientations stratégiques"),
        ("Communication", "Compétences en communication interne")
    ]
    
    for param_name, param_desc in agent_params:
        param_data = [
            ("param", param_name),
            ("description", param_desc)
        ]
        bdd_add_records("agentParams", param_data)
        param_id = get_last_insert_id("agentParams")
        
        agent_param_value = "Expert"  # Par exemple, la valeur peut être définie plus dynamiquement
        bdd_add_records("agentsParams", [
            ("agentId", agent_id),
            ("paramId", param_id),
            ("paramValue", agent_param_value)
        ])

    # 6. Créer le hook qui déclenche les actions after_create_department
    hook_model = os.path.join("./backend/src/services/Technology_Department/automation/models", "after_create_department.py")
    
    if os.path.exists(hook_model):
        hook("after_create_department")
    else:
        print(f"Le modèle de hook pour after_create_department est introuvable : {hook_model}")

    print(f"Département {department} créé avec succès, les actions after_create_department ont été déclenchées.")
