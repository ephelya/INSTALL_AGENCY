import os
from backend.src.services.Technology_Department.database_management.actions.delete_record import delete_record

def hook_delete(hookId):
    """
    Supprime un hook et toutes les associations d'actions dans hooksActions.

    :param hookId: L'ID du hook à supprimer
    """
    # Supprimer les actions associées au hook dans hooksActions
    delete_record("hooksActions", {"hookId": hookId})
    
    # Supprimer le hook dans la table hooks
    delete_record("hooks", {"id": hookId})
    
    print(f"Hook {hookId} et ses actions associées ont été supprimés")
