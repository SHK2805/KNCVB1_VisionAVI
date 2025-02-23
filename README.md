# KNCVB1 Vision AVI
## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
    1. [Prerequisites](#prerequisites)
        1. [Conda](#conda)
        2. [Github](#github)
3. [Environment File](#environment-file)

## Introduction
* This is the KNCVB1 Vision AVI project

## Setup

### Prerequisites
#### Conda
* Install [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
* Create a new conda environment
```bash
conda create --name kncvb1-vision-avi python=3.10
```
* List the conda environments
```bash
conda env list
```
* Activate the conda environment
```bash
conda activate kncvb1-vision-avi
```
* Install the required packages
```bash
pip install -r requirements.txt
```
* Deactivate the conda environment
```bash
conda deactivate
```

#### Github
* Clone the repository
```bash
git clone https://github.com/SHK2805/KNCVB1_VisionAVI.git
```
* Change the directory
```bash
cd KNCVB1_VisionAVI
```
* Create a new branch:
```bash
git checkout -b <branch-name>
```
* Add the changes:
```bash
git add .
```
* Commit the changes:
```bash
git commit -m "<commit message>"
```
* Push the changes and track the remote branch:
```bash
git push -u origin <branch-name>
```
* Create a pull request from the branch to the main branch:
```bash
git <pull-request>
```
* Merge the pull request:
```bash
git merge <branch-name>
```
* Delete the branch:
```bash
git branch -d <branch-name>
```
* Pull the changes from the remote repository:
```bash
git pull
```

## Environment File
* Create a new environment file (.env) in the root directory. 
* This contains the environment variables that are used in the project.
* Add this to the `.gitignore` file so that it is not pushed to the remote repository. 
* We can use the python-dotenv package to load the environment variables from the .env file. 
* Use the below code to load the environment variables from the `.env` file:
```python
from dotenv import load_dotenv
import os
# Load the environment variables from the .env file
load_dotenv()
var = os.getenv("VAR_NAME")
```

## Folder Structure
* The folder structure of the project can be created using the `template.py` file.
* Install the `setuptools` package or add it to the `requirements.txt` file.
```bash
pip install setuptools
```
* The `setup.py` file contains the configuration for the folder structure.
* Run the below command to create the folder structure:
```bash
python setup.py
# or
pip install requirements.txt
```



