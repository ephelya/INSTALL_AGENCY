import os
from backend.src.services.Technology_Department.database_management import bdd_get_records

def get_logs_by_project_id(project_id):
    """
    Récupère la liste des logs associés à un projet.

    :param project_id: L'ID du projet
    :return: Une liste de dictionnaires représentant les logs ou une liste vide s'il n'y a aucun log
    """
    logs = bdd_get_records(
        "logs JOIN projectsLogs ON logs.id = projectsLogs.logId", 
        conditions={"projectsLogs.projectId": project_id},
        columns=["logs.id", "logs.name", "logs.description", "logs.url"]
    )
    
    if logs:
        print(f"Logs trouvés pour le projet {project_id} : {logs}")
        return logs
    else:
        print(f"Aucun log trouvé pour le projet {project_id}")
        return []
