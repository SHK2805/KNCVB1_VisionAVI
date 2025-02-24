import os
from pathlib import Path
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

def create_directory(path: Path):
    if not path.exists():
        os.makedirs(path, exist_ok=True)
        logging.info(f"Creating directory: {path}")
    else:
        logging.info(f"Directory {path} already exists")


def create_file(filepath: Path):
    if not filepath.exists() or filepath.stat().st_size == 0:
        filepath.touch()
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath.name} already exists")

def create_project_structure(project_name: str) -> bool:
    try:
        data_folder_name: str = "phishingdata"
        list_of_files = [
            # general files
            "template.py",
            "setup.py",
            ".env",
            ".gitignore",
            "requirements.txt",
            "README.md",
            # logs
            f"logs",
            # api
            f"api/__init__.py",
            # data
            f"data",
            # database
            f"database/__init__.py",
            f"database/cloud/__init__.py",
            f"database/cloud/cloudformation_template.yaml",
            f"database/cloud/deploy_stack.py",
            f"database/cloud/constants.py",
            # research
            f"research/__init__.py",
            f"research/database/operations/__init__.py",
            # utils
            f"utils/__init__.py",
            f"utils/db_utils.py",
            # logging
            f"logger/__init__.py",
            f"logger/logger.py",
            # exception
            f"exception/__init__.py",
            f"exception/exception.py",
            # init
            f"__init__.py",
            # clean
            "clean.py",
        ]

        for filepath in list_of_files:
            filepath = Path(filepath)
            filedir = filepath.parent

            # files
            if filepath.name in ['setup.py', 'requirements.txt', 'README.md', '.gitignore','.env']:
                create_file(filepath)
                continue

            # Create directories
            create_directory(filedir)

            # Create files if they do not exist or are empty
            if filepath.suffix:  # Check if it's a file (has a suffix)
                create_file(filepath)
            else:
                create_directory(filepath)
    except Exception as e:
        logging.error(f"Error in creating project structure: {e}")
        return False
    return True

if __name__ == "__main__":
    cv_project_name = "kncvb1_vision_avi"
    create_project_structure(cv_project_name)
    logging.info(f"Project structure created for {cv_project_name}")