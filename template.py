import os
import logging
from pathlib import Path



logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "math_ai_app"

list_of_files = [

    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/settings.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/core/__init__.py",
    f"src/{project_name}/core/problem_solver.py",
    f"src/{project_name}/core/learning.py",
    f"src/{project_name}/core/quiz_generator.py",
    f"src/{project_name}/core/assistant.py",
    f"src/{project_name}/db/__init__.py",
    f"src/{project_name}/db/database.py",
    f"src/{project_name}/db/schems.sql"

    

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok= True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating a empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exixts")