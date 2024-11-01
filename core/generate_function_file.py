import os

def generate_function_file(department, function_name, services_path, metadatas, imports, inputs, description, body=""):
    template_path = os.path.join(os.getcwd(), "Templates", "function_template.txt")
    
    with open(template_path, "r") as template_file:
        template_content = template_file.read()

    file_content = template_content.replace("<function_name>", function_name)
    file_content = file_content.replace("<metadatas>", metadatas)
    file_content = file_content.replace("<imports>", imports)
    file_content = file_content.replace("<services_path>", services_path)
    file_content = file_content.replace("<department>", department)
    file_content = file_content.replace("<inputs>", inputs)
    file_content = file_content.replace("<description>", description)
    file_content = file_content.replace("<body>", body)

    function_dir = os.path.join("Departments", department, "actions")
    os.makedirs(function_dir, exist_ok=True)
    function_file_path = os.path.join(function_dir, f"{function_name}.py")

    with open(function_file_path, "w") as function_file:
        function_file.write(file_content)

    print(f"Fichier de fonction généré : {function_file_path}")
