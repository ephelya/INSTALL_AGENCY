import os
from datetime import datetime

def add_metadata(file_type, file_name, author, file_path, file_version, file_mission, inputs_params, output_params):
    """
    Génère des métadonnées formatées pour le fichier de fonction.
    """
    last_update = datetime.now().strftime("%Y%m%d-%H%M")
    metadata_content = f"""# file_type: {file_type}
# file_name: {file_name}
# last_update: {last_update}
# author: {author}
# file_path: {file_path}
# file_version: {file_version}
# file_mission: {file_mission}
# inputs_params: {inputs_params}
# output_params: {output_params}
"""
    return metadata_content

def generate_function_file(department, function_name, services_path, file_type, author, file_version, file_mission, imports, inputs_params, output_params, description, body=""):
    """
    Génère le fichier de fonction avec les métadonnées, imports et corps de fonction spécifiés.
    """
    # Génération des métadonnées
    metadatas = add_metadata(
        file_type=file_type,
        file_name=function_name,
        author=author,
        file_path=f"{services_path}/{department}/actions/{function_name}.py",
        file_version=file_version,
        file_mission=file_mission,
        inputs_params=inputs_params,
        output_params=output_params
    )
    
    # Chemin vers le modèle de template
    template_path = os.path.join(os.getcwd(), "Templates", "function_template.txt")
    
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    # Remplacement des placeholders dans le modèle
    imports_content = "\n".join(f"import {imp}" for imp in imports)
    file_content = template_content.replace("<function_name>", function_name)
    file_content = file_content.replace("<metadatas>", metadatas)
    file_content = file_content.replace("<imports>", imports_content)
    file_content = file_content.replace("<inputs>", ", ".join(inputs_params))
    file_content = file_content.replace("<description>", description)
    file_content = file_content.replace("<body>", body)

    # Création du répertoire et écriture du fichier
    function_dir = os.path.join("Departments", department, "actions")
    os.makedirs(function_dir, exist_ok=True)
    function_file_path = os.path.join(function_dir, f"{function_name}.py")

    with open(function_file_path, "w") as function_file:
        function_file.write(file_content)

    print(f"Fichier de fonction généré : {function_file_path}")
