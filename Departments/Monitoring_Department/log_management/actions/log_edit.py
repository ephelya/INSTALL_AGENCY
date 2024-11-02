import os
from backend.src.services.Technology_Department.database_management import bdd_update_records

def log_edit(log_id, new_description):
    """
    Modifie la description d'un log existant.

    :param log_id: L'ID du log à modifier
    :param new_description: La nouvelle description du log
    """
    update_data = {"description": new_description}
    conditions = {"id": log_id}
    
    bdd_update_records("logs", update_data, conditions)
    print(f"Description du log {log_id} modifiée à '{new_description}'")

