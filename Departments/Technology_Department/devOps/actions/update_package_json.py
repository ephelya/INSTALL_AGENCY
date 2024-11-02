import os
import json
def update_package_json(frontend_path):
    package_json_path = os.path.join(frontend_path, "package.json")
    if os.path.exists(package_json_path):
        with open(package_json_path, "r+") as f:
            package_data = json.load(f)
            package_data["dependencies"]["react-helmet"] = "^6.1.0"
            package_data["dependencies"]["react-router-dom"] = "^5.2.0"
            f.seek(0)
            json.dump(package_data, f, indent=2)
            f.truncate()
        print("Fichier package.json mis à jour")
    else:
        print("Avertissement : package.json non trouvé")
