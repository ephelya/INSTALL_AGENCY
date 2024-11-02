import os
import json
from files.backend.src.services.Technology_Department.architecture.actions.create_file import create_file
from files.backend.src.services.Technology_Department.devOps.actions.run_command import run_command


def setup_backend(backend_path, project_name):
    # Création du fichier server.js
    server_js_content = """
const express = require('express');
const path = require('path');
const app = express();
let PORT = process.env.PORT || 3000;

app.use(express.static(path.join(__dirname, '../frontend')));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../frontend', 'index.html'));
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
    """
    create_file(os.path.join(backend_path, "server.js"), server_js_content)

    # Création du fichier package.json pour le backend
    backend_package = {
        "name": f"{project_name}-backend",
        "version": "1.0.0",
        "main": "server.js",
        "dependencies": {
            "express": "^4.17.1"
        },
        "scripts": {
            "start": "node server.js"
        }
    }
    with open(os.path.join(backend_path, "package.json"), "w") as f:
        json.dump(backend_package, f, indent=2)

    # Installation des dépendances backend
    print("Installation des dépendances backend...")
    if run_command("npm install", cwd=backend_path):
        print("Dépendances backend installées avec succès")
    else:
        print("Échec de l'installation des dépendances backend")
