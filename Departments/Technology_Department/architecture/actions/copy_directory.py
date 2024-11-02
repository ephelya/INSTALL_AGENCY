#copy_directory.py

import os
import shutil

def copy_directory(src, dest):
        """
        Copie récursivement la structure de répertoires et les fichiers de src vers dest.
        """
        if not os.path.exists(dest):
            os.makedirs(dest)
        
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dest, item)
            if os.path.isdir(s):
                copy_directory(s, d)
            else:
                shutil.copy2(s, d)
        print(f"Structure copiée de {src} vers {dest}")
