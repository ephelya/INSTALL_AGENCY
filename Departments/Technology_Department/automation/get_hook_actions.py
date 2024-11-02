import os
from backend.src.services.Technology_Department.database_management import bdd_get_records

def get_hook_actions(hook_name):
    # Simule la récupération depuis la base de données
    actions = bdd_get_records("hooksActions", {"hook_name": hook_name})
    return actions
