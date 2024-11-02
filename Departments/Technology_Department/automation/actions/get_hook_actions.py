import os
from files.backend.src.services.Technology_Department.database_management.actions.bdd_get_records_with_join import bdd_get_records_with_join
def get_hook_actions(hook_name):
    """
    Récupère les actions associées à un hook spécifique depuis la base de données.

    :param hook_name: Nom du hook (par ex: 'before_install', 'after_install')
    :return: Une liste d'actions associées au hook
    """
    # Conditions pour trouver les hooks associés
    conditions = {"hooks.name": hook_name}
    
    # Appel de la fonction avec jointure entre hooksActions et actions
    actions = bdd_get_records_with_join(
        table="hooksActions", 
        join_table="actions", 
        join_condition="hooksActions.action_id = actions.id",
        conditions=conditions,
        columns=["actions.action_name", "actions.action_path"]
    )
    
    if actions:
        print(f"Actions trouvées pour le hook {hook_name}: {actions}")
        return actions
    else:
        print(f"Aucune action trouvée pour le hook {hook_name}")
        return []
