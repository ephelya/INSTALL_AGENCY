import os
from backend.src.services.Technology_Department.database_management.actions.bdd_add_records import bdd_add_records
from backend.src.services.Technology_Department.database_management.actions.get_last_insert_id import get_last_insert_id


def hook_create(hook, folder, description, projectId):
    """
    Crée un fichier hook avec le nom du hook, enregistre sa description dans la base de données,
    et associe le hook à un projet.

    :param hook: Nom du hook (par ex: after_install)
    :param folder: Dossier dans lequel créer le hook (par défaut: src/hooks/)
    :param description: Description du hook
    :param projectId: ID du projet auquel ce hook est associé
    """
    # Construire le chemin du fichier hook
    hook_path = os.path.join(folder, f"{hook}.py")

    # Créer le dossier s'il n'existe pas
    os.makedirs(folder, exist_ok=True)

    # Contenu du fichier hook
    hook_content = f'''
# Hook: {hook}
# Description: {description}

def {hook}():
    print("{hook} triggered")

# Ajoutez ici la logique du hook
'''

    # Créer le fichier hook avec le contenu
    with open(hook_path, 'w') as hook_file:
        hook_file.write(hook_content)
    print(f"Hook créé : {hook_path}")

    # Enregistrer le hook dans la table hooks
    hook_data = [
        ("name", hook),
        ("description", description),
        ("url", hook_path)
    ]
    bdd_add_records("hooks", hook_data)

    # Obtenir l'ID du hook nouvellement inséré
    hookId = get_last_insert_id("hooks")

    # Associer le hook au projet dans la table projectsHooks
    project_hook_data = [
        ("projectId", projectId),
        ("hookId", hookId)
    ]
    bdd_add_records("projectsHooks", project_hook_data)

    print(f"Hook '{hook}' ajouté et associé au projet ID {projectId}")
