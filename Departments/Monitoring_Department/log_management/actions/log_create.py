import os
from backend.src.services.Technology_Department.database_management import bdd_add_records

def log_create(log, datetime, userId, logType, url=None):
    """
    Ajoute un log à la base de données.

    :param log: Contenu ou description du log
    :param datetime: Datetime de l'événement (peut être 'CURRENT_TIMESTAMP' pour l'heure actuelle)
    :param userId: ID de l'utilisateur associé au log
    :param logType: Type d'action ou d'événement lié au log
    :param url: URL ou chemin associé au log (optionnel)
    """
    # Chemin par défaut pour les logs, modifiable si nécessaire
    if url is None:
        url = os.path.join("src", "logs", f"{logType}.log")

    # Données à insérer dans la table logs
    log_data = [
        ("datetime", datetime),
        ("action", logType),
        ("log", log),
        ("url", url),
        ("userId", userId)
    ]
    
    # Ajouter le log à la base de données
    bdd_add_records("logs", log_data)

    print(f"Log ajouté : {logType}, {datetime}, utilisateur ID : {userId}")
