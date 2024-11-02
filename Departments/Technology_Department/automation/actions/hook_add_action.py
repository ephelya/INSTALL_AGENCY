import os
from backend.src.services.Technology_Department.database_management.actions.bdd_add_records import bdd_add_records
from backend.src.services.Technology_Department.database_management.actions.bdd_get_records import bdd_get_records


def hook_add_action(hookId, actionId, order=None):
    """
    Associe une action à un hook avec un ordre d'exécution optionnel.

    :param hookId: L'ID du hook auquel associer l'action
    :param actionId: L'ID de l'action à associer
    :param order: L'ordre d'exécution de l'action (facultatif)
    """
    # Utiliser bdd_get_records pour vérifier si l'association existe déjà
    existing = bdd_get_records(
        table="hooksActions", 
        conditions={"hookId": hookId, "actionId": actionId}
    )

    if existing:
        print(f"L'action {actionId} est déjà associée au hook {hookId}")
        return

    # Ajouter une nouvelle association dans hooksActions
    hook_action_data = [
        ("hookId", hookId),
        ("actionId", actionId),
        ("order", order)
    ]
    bdd_add_records("hooksActions", hook_action_data)
    print(f"Action {actionId} ajoutée au hook {hookId} avec l'ordre {order}")
