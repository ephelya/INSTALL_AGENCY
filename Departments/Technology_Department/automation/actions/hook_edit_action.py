import os
from backend.src.services.Technology_Department.database_management.actions.bdd_update_records import bdd_update_records


def hook_edit_action(hookId, actionId, newOrder):
    """
    Modifie l'ordre d'une action associée à un hook.

    :param hookId: L'ID du hook
    :param actionId: L'ID de l'action à modifier
    :param newOrder: Le nouvel ordre d'exécution de l'action
    """
    update_data = {"order": newOrder}
    conditions = {"hookId": hookId, "actionId": actionId}
    
    bdd_update_records("hooksActions", update_data, conditions)
    print(f"Ordre de l'action {actionId} modifié à {newOrder} pour le hook {hookId}")



