#hook_action_execute.py 
import importlib

def hook_action_execute(action):
    try:
        module_name = action['module']
        function_name = action['function']
        module = importlib.import_module(module_name)
        function = getattr(module, function_name)
        function()  # Exécution de la fonction
    except (ImportError, AttributeError) as e:
        print(f"Erreur lors du chargement ou de l'exécution de l'action {action['name']}: {e}")
