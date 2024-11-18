import os           ##provides functions to interact withoperating system,such as managing files,directories,environment variables.
from pathlib import Path            ##simplifies file and directory handling making path manipulations more intuitive and readable
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')  ##shows log msg and time


project_name = 'ChickenDisease'

list_of_files = [
    ".github/workflows/.gitkeep",               ##doesn't keep any folder empty as github doesnt track empty folder
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
    
     
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)     ##separates file and filename
    
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")
        
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating Empty file: {filepath}")
            
    else:
        logging.info(f"{filename} already exists.")