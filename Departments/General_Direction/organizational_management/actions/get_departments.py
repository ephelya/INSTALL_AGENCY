from backend.src.services.Technology_Department.database_management import bdd_get_records

def get_departments(department_id=None):
    """
    Récupère la liste des départements, leurs services, agents et fichiers department_overview.txt depuis la base de données.

    :param department_id: Optionnel, l'ID du département à récupérer. Si None, récupère tous les départements.
    :return: Liste des départements avec leurs services, agents, et informations associées.
    """
    departments_data = []

    # Construire la requête pour récupérer les départements
    conditions = {} if department_id is None else {"id": department_id}
    departments = bdd_get_records("departments", conditions)

    for department in departments:
        department_id = department["id"]
        department_info = {
            "department_id": department_id,
            "name": department["name"],
            "role": department["role"],
            "services": [],
            "agents": [],
            "department_overview": department.get("overview", "")
        }

        # Récupérer les services du département
        services = bdd_get_records("departmentsServices", {"departmentId": department_id})
        for service in services:
            service_info = {
                "service_id": service["id"],
                "service_name": service["service"],
                "role": service["role"]
            }
            department_info["services"].append(service_info)

        # Récupérer les agents du département
        agents = bdd_get_records("agents", {"departmentId": department_id})
        for agent in agents:
            agent_info = {
                "agent_id": agent["id"],
                "name": agent["name"],
                "mission": agent["mission"]
            }
            department_info["agents"].append(agent_info)

        departments_data.append(department_info)

    return departments_data
