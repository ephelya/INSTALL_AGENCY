from core.generate_function_file import generate_function_file

class AIAgent:
    def __init__(self):
        print("Agent IA initialisé pour la création de fonctions")

    def create_function(self, department, function_name, services_path, file_type, author, file_version, file_mission, imports, inputs_params, output_params, description, body=""):
        """
        Utilise generate_function_file pour créer un fichier de fonction dans le département spécifié.
        """
        generate_function_file(
            department=department,
            function_name=function_name,
            services_path=services_path,
            file_type=file_type,
            author=author,
            file_version=file_version,
            file_mission=file_mission,
            imports=imports,
            inputs_params=inputs_params,
            output_params=output_params,
            description=description,
            body=body
        )

# Exemple d'utilisation directe si on exécute AIAgent.py seul
if __name__ == "__main__":
    agent = AIAgent()
    agent.create_function(
        department="General_Direction",
        function_name="supervise_agents",
        services_path="Departments",
        file_type="action",
        author="General_Direction",
        file_version="1.0",
        file_mission="Supervise la liste des agents",
        imports=["os"],
        inputs_params=["agent_list"],
        output_params=["status"],
        description="Supervise la liste des agents et renvoie leur statut.",
        body="# Code de supervision des agents"
    )
