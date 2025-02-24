# KNCVB1 Vision AVI
## Table of Contents
1. [Introduction](#introduction)
2. [Setup](#setup)
    1. [Prerequisites](#prerequisites)
        1. [Conda](#conda)
        2. [Github](#github)
3. [Environment File](#environment-file)
4. [Folder Structure](#folder-structure)
5. [Logging](#logging)
6. [Exception](#exception)
7. [Infrastructure](#infrastructure)

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

#### AWSCLI
* This is needed if you are deploying or using AWS services
* Before deploying to the cloud, make sure the `awscli` is installed
  * The `awscli` is a command-line tool that provides commands for interacting with AWS services
  * To install the `awscli` package, run the following command:
  ```bash
  pip install awscli
  ```
  * To configure the `awscli`, run the following command:
  * Open the terminal and run the following command
  ```bash
  aws configure
  ```
    * Enter the following details:
        * AWS Access Key ID
        * AWS Secret Access Key
        * Default region name
        * Default output format
* Before deploying to the cloud, make sure the `boto3` and `botocore` packages are installed
* Add `boto3` and `botocore` to the `requirements.txt` file
  * The `boto3` is the AWS SDK for Python
  * The `botocore` is the low-level, core functionality of the AWS SDK for Python
* To install the `boto3` and `botocore` packages manually, run the following command:
```bash
pip install boto3 botocore
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

## Logging
* A custom logger is written in the `logger/logger.py` file.
* This writes the logs to the `logs` directory with the log file name as the current date and time.
* **TODO**: We can update this to read from the `config.yaml` file 
* Add this `logs` folder to `.gitignore` to avoid pushing logs to the git repository.

## Exception
* A custom exception is written in the `exception/exception.py` file.
* This is used to raise exceptions with a custom message.

## Infrastructure
* All the infrastructure code is written in the `database` directory.
* The infrastructure is created in `aws` using CloudFormation stack
* The code for the stack is written in the `database/cloud` folder
  * cloudformation_template.yaml
  * deploy_stack.py
* The values needed for the stack are written. We can move this to `config.yaml` file later
  * constants.py
  * .env
* Below are the various components created in the aws stack
  * s3 bucket
  * ec2 instance
  * sqllite is installed in ec2 through user data in cloudformation stack
    * To check if sqllite is installed and running
      * ssh into the ec2 instance
      * run the below command.
      ```bash
      sqlite3 --version
      ```
      * It may take sometime for the sqlite to be installed and running, so wait and try again
      * To connect the sqlite database, run the below command
      ```bash
      # ssh to ec2 instance
      ssh -i <keypair.pem> ec2-user@<public-ip>
      sqllite3 ex1
      ```
  * The ec2 instance is created in a public subnet
  * The security group is created to allow traffic on port 22 and 80
  * The key pair is created to ssh into the ec2 instance
    * I am giving the name of the keypair in my `.env` file as `KEY_PAIR_NAME`