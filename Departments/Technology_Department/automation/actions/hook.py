# hook.py
import os
from files.backend.src.services.Technology_Department.automation.actions.hook_action_execute import hook_action_execute
from files.backend.src.services.Technology_Department.automation.actions.get_hook_actions import get_hook_actions

def hook(hook_name):
    actions = get_hook_actions(hook_name)
    if not actions:
        print(f"Aucune action trouvée pour le hook {hook_name}")
        return

    for action in actions:
        try:
            hook_action_execute(action)
        except Exception as e:
            print(f"Erreur lors de l'exécution de l'action {action}: {e}")
