import os
from backend.src.services.Technology_Department.database_management.actions.bdd_add_records  import bdd_add_records
from backend.src.services.Technology_Department.database_management.actions.get_last_insert_id import get_last_insert_id
from backend.src.services.Technology_Department.database_management.actions.bdd_get_records import bdd_get_records
from backend.src.services.Technology_Department.database_management.actions.bdd_update_records  import bdd_update_records
from backend.src.services.Technology_Department.database_management.actions.delete_record  import delete_record

def cronCreate(cron, folder, description, projectId):
    """
    Crée un fichier cron avec le nom du cron, enregistre sa description dans la base de données,
    et associe le cron à un projet.

    :param cron: Nom du cron (par ex: data_backup)
    :param folder: Dossier dans lequel créer le cron (par ex: src/crons/)
    :param description: Description du cron
    :param projectId: ID du projet auquel ce cron est associé
    """
    # Construire le chemin du fichier cron
    cron_path = os.path.join(folder, f"{cron}.py")

    # Créer le dossier s'il n'existe pas
    os.makedirs(folder, exist_ok=True)

    # Contenu du fichier cron
    cron_content = f'''
# Cron: {cron}
# Description: {description}

def {cron}():
    print("{cron} triggered")

# Ajoutez ici la logique du cron
'''

    # Créer le fichier cron avec le contenu
    with open(cron_path, 'w') as cron_file:
        cron_file.write(cron_content)
    print(f"Cron créé : {cron_path}")

    # Enregistrer le cron dans la table crons
    cron_data = [
        ("name", cron),
        ("description", description),
        ("url", cron_path)
    ]
    bdd_add_records("crons", cron_data)

    # Obtenir l'ID du cron nouvellement inséré
    cronId = get_last_insert_id("crons")

    # Associer le cron au projet dans la table projectsCrons
    project_cron_data = [
        ("projectId", projectId),
        ("cronId", cronId)
    ]
    bdd_add_records("projectsCrons", project_cron_data)

    print(f"Cron '{cron}' ajouté et associé au projet ID {projectId}")
def cronEditAction(cronId, actionId, newOrder):
    """
    Modifie l'ordre d'une action associée à un cron.

    :param cronId: L'ID du cron
    :param actionId: L'ID de l'action à modifier
    :param newOrder: Le nouvel ordre d'exécution de l'action
    """
    update_data = {"order": newOrder}
    conditions = {"cronId": cronId, "actionId": actionId}
    
    bdd_update_records("cronsActions", update_data, conditions)
    print(f"Ordre de l'action {actionId} modifié à {newOrder} pour le cron {cronId}")
    """
    Modifie l'ordre d'une action associée à un cron.

    :param cronId: L'ID du cron
    :param actionId: L'ID de l'action à modifier
    :param newOrder: Le nouvel ordre d'exécution de l'action
    """
    update_data = {"order": newOrder}
    conditions = {"cronId": cronId, "actionId": actionId}
    
    bdd_update_records("cronsActions", update_data, conditions)
    print(f"Ordre de l'action {actionId} modifié à {newOrder} pour le cron {cronId}")
def cronDelete(cronId):
    """
    Supprime un cron et toutes les associations d'actions dans cronsActions.

    :param cronId: L'ID du cron à supprimer
    """
    # Supprimer les actions associées au cron dans cronsActions
    delete_record("cronsActions", {"cronId": cronId})
    
    # Supprimer le cron dans la table crons
    delete_record("crons", {"id": cronId})
    
    print(f"Cron {cronId} et ses actions associées ont été supprimés")
    """
    Supprime un cron et toutes les associations d'actions dans cronsActions.

    :param cronId: L'ID du cron à supprimer
    """
    # Supprimer les actions associées au cron dans cronsActions
    delete_record("cronsActions", {"cronId": cronId})
    
    # Supprimer le cron dans la table crons
    delete_record("crons", {"id": cronId})
    
    print(f"Cron {cronId} et ses actions associées ont été supprimés")
def getCronsByProjectId(projectId):
    """
    Récupère la liste des crons associés à un projet.

    :param projectId: L'ID du projet
    :return: Une liste de dictionnaires représentant les crons ou une liste vide s'il n'y a aucun cron
    """
    crons = bdd_get_records(
        "crons JOIN projectsCrons ON crons.id = projectsCrons.cronId", 
        conditions={"projectsCrons.projectId": projectId},
        columns=["crons.id", "crons.name", "crons.description", "crons.url"]
    )
    
    if crons:
        print(f"Crons trouvés pour le projet {projectId} : {crons}")
        return crons
    else:
        print(f"Aucun cron trouvé pour le projet {projectId}")
        return []
def cronAddAction(cronId, actionId, order=None):
    """
    Associe une action à un cron avec un ordre d'exécution optionnel.

    :param cronId: L'ID du cron auquel associer l'action
    :param actionId: L'ID de l'action à associer
    :param order: L'ordre d'exécution de l'action (facultatif)
    """
    # Utiliser bddGetRecords pour vérifier si l'association existe déjà
    existing = bdd_get_records(
        table="cronsActions", 
        conditions={"cronId": cronId, "actionId": actionId}
    )

    if existing:
        print(f"L'action {actionId} est déjà associée au cron {cronId}")
        return

    # Ajouter une nouvelle association dans cronsActions
    cron_action_data = [
        ("cronId", cronId),
        ("actionId", actionId),
        ("order", order)
    ]
    bdd_add_records("cronsActions", cron_action_data)
    print(f"Action {actionId} ajoutée au cron {cronId} avec l'ordre {order}")
