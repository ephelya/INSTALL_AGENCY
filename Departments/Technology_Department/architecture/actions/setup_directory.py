import os 

def setup_directory(self):
        # Setup : Créer les dossiers temporaires pour les tests
        self.src = "test_src"
        self.dest = "test_dest"
        os.makedirs(self.src, exist_ok=True)

        # Créer un fichier test dans src
        with open(os.path.join(self.src, "test_file.txt"), 'w') as f:
            f.write("Test content")