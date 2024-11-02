import os
from files.backend.src.services.Technology_Department.architecture.actions.create_file import create_file

def create_react_file(frontend_path):

    # Obtenir le chemin absolu du fichier actuel et remonter au répertoire templates
    current_directory = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.abspath(os.path.join(current_directory, "../../../../../../../templates"))
    print(f"templates_dir récup {templates_dir} ")

    # Vérification si le répertoire templates existe
    if not os.path.exists(templates_dir):
        print(f"Le répertoire {templates_dir} n'existe pas.")
        return

    # Récupérer le contenu de indexPage.js
    with open(os.path.join(templates_dir, "indexPage.js"), "r") as index_page_file:
        index_page_content = index_page_file.read()

    # Créer IndexPage.js
    create_file(os.path.join(frontend_path, "src", "pages", "IndexPage.js"), index_page_content)

    # Récupérer le contenu de AdminPage.js
    with open(os.path.join(templates_dir, "AdminPage.js"), "r") as admin_page_file:
        admin_page_content = admin_page_file.read()

    # Créer AdminPage.js
    create_file(os.path.join(frontend_path, "src", "pages", "AdminPage.js"), admin_page_content)

    # Création de App.js (Remplace le fichier existant)
    app_js_content = """
import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import IndexPage from './pages/IndexPage';
import AdminPage from './pages/AdminPage';

function App() {
  const sections = [
    { content: 'Section 1 content', testing: true, test_version: '1.0' },
    { content: 'Section 2 content' }
  ];

  const title = "My Website";
  const menuLinks = ["Home", "About", "Services", "Contact"];
  const description = "Welcome to My Website";

  return (
    <Router>
      <Switch>
        <Route 
          exact path="/" 
          render={() => (
            <IndexPage 
              title={title} 
              menuLinks={menuLinks} 
              description={description} 
              sections={sections} 
            />
          )} 
        />
        <Route path="/admin" render={() =>  <IndexPage 
              title={title} 
              menuLinks={menuLinks} 
              description={description} 
              sections={sections} 
            />} />
      </Switch>
    </Router>
  );
}

export default App;
    """
    # Création du fichier App.js, remplacement de celui par défaut
    create_file(os.path.join(frontend_path, "src", "App.js"), app_js_content)

    # Création des composants partiels
    partial_components = ['Header', 'Footer', 'Sidebar', 'Head']
    for component in partial_components:
        component_path = os.path.join(frontend_path, "src", "templates", "partials", f"{component}.js")
        if not os.path.exists(component_path):
            component_content = f"""
import React from 'react';

const {component} = () => {{
    return (
        <div>{component} Component</div>
    );
}};

export default {component};
            """
            # Remplace {component} par le nom du composant actuel
            component_content = component_content.replace("{component}", component)
            create_file(component_path, component_content)
