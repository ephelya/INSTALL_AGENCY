from core.generate_function_file import generate_function_file

class AIAgent:
    def __init__(self):
        print("Agent IA initialisé pour la création de fonctions")

    def create_function(self, department, function_name, services_path, metadatas, imports, inputs, description, body=""):
        """
        Utilise generate_function_file pour créer un fichier de fonction dans le département spécifié.
        """
        generate_function_file(
            department=department,
            function_name=function_name,
            services_path=services_path,
            metadatas=metadatas,
            imports=imports,
            inputs=inputs,
            description=description,
            body=body
        )

# Exemple d'utilisation directe si on exécute AIAgent.py seul
if __name__ == "__main__":
    agent = AIAgent()
    agent.create_function(
        department="General_Direction",
        function_name="supervise_agents",
        services_path="services",
        metadatas="# Metadata: version=1.0, author='General_Direction'",
        imports="import os",
        inputs="agent_list",
        description="Supervise la liste des agents.",
        body="# Code de supervision des agents"
    )
