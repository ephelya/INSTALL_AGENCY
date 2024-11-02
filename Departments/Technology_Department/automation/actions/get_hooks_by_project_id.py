import os
from backend.src.services.Technology_Department.database_management.actions.bdd_get_records import bdd_get_records


def get_hooks_by_project_id(projectId):
    """
    Récupère la liste des hooks associés à un projet.

    :param projectId: L'ID du projet
    :return: Une liste de dictionnaires représentant les hooks ou une liste vide s'il n'y a aucun hook
    """
    hooks = bdd_get_records(
        "hooks JOIN projectsHooks ON hooks.id = projectsHooks.hookId", 
        conditions={"projectsHooks.projectId": projectId},
        columns=["hooks.id", "hooks.name", "hooks.description", "hooks.url"]
    )
    
    if hooks:
        print(f"Hooks trouvés pour le projet {projectId} : {hooks}")
        return hooks
    else:
        print(f"Aucun hook trouvé pour le projet {projectId}")
        return []
