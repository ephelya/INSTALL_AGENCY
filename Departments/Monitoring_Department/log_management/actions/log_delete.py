import os

from backend.src.services.Technology_Department.database_management import delete_record

def log_delete(log_id):
    """
    Supprime un log et toutes les associations dans projectsLogs.

    :param log_id: L'ID du log à supprimer
    """
    # Supprimer les associations avec les projets dans projectsLogs
    delete_record("projectsLogs", {"logId": log_id})
    
    # Supprimer le log dans la table logs
    delete_record("logs", {"id": log_id})
    
    print(f"Log {log_id} et ses associations au projet ont été supprimés")
