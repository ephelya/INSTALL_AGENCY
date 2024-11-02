#database_setup
import os
from files.backend.src.services.Technology_Department.database_management.actions.execute_setup_script import execute_setup_script

def database_setup (db_install_file):
    execute_setup_script(db_install_file)