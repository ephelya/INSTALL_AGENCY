import os
import shutil
import unittest
from files.backend.src.services.Technology_Department.architecture.actions.copy_directory import copy_directory
from files.backend.src.services.Technology_Department.architecture.actions.setup_directory import setup_directory


class TestCopyDirectory(unittest.TestCase):





    def test_copy_directory_success(self):
        copy_directory(self.src, self.dest)

        # Vérifier si le répertoire et le fichier ont été copiés
        self.assertTrue(os.path.exists(self.dest))
        self.assertTrue(os.path.exists(os.path.join(self.dest, "test_file.txt")))

    def test_copy_directory_missing_destination(self):
        # Test avec une destination vide
        with self.assertRaises(OSError):  # On attend une exception car le dossier dest est vide
            copy_directory(self.src, "")

if __name__ == '__main__':
    unittest.main()
