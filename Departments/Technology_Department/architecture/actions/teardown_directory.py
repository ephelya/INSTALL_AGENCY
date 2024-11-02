import os 
 
def teardown_directory(self):
    # Teardown : Supprimer les dossiers après les tests
    if os.path.exists(self.src):
        shutil.rmtree(self.src)
    if os.path.exists(self.dest):
        shutil.rmtree(self.dest)