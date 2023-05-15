# Databricks notebook source
import subprocess
import os
def is_git_repository():
    try:
        subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'])
        return True
    except subprocess.CalledProcessError:
        return False
'''
def get_git_commit_id():
    if not is_git_repository():
        os.chdir()
        return None

    try:
        commit_id = subprocess.check_output(['git', 'rev-parse', 'HEAD']).strip().decode('utf-8')
        return commit_id
    except subprocess.CalledProcessError:
        return None

# Get the Git commit ID
commit_id = get_git_commit_id()
'''
# Print the commit ID
if commit_id:
    print("Git commit ID:", commit_id)
else:
    print("Unable to retrieve Git commit ID.")


# COMMAND ----------

# MAGIC %sh
# MAGIC pwd

# COMMAND ----------

import os

# Specify the target directory
target_directory = '/Workspace/Repos/sneha.ck@databricks.com/test-repo'

# Change the current working directory
os.chdir(target_directory)

# Verify the new working directory
current_directory = os.getcwd()
print("Current working directory:", current_directory)


# COMMAND ----------

import os

# Get the directory of the script
script_directory = os.path.dirname(os.path.abspath()

# Print the script directory
print("Script directory:", script_directory)


# COMMAND ----------

subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree'])

# COMMAND ----------

import subprocess

def is_git_repository():
    try:
        output = subprocess.check_output(['git', 'rev-parse', '--is-inside-work-tree']).strip().decode('utf-8')
        return output == 'true'
    except subprocess.CalledProcessError:
        return False

# Check if the current directory is inside a Git repository
if is_git_repository():
    print("Current directory is inside a Git repository")
else:
    print("Current directory is not inside a Git repository")


# COMMAND ----------

import os
import subprocess

def move_to_git_repo():
    try:
        # Get the path to the root directory of the Git repository
        git_root_path = subprocess.check_output(['git', 'rev-parse', '--show-toplevel']).strip().decode('utf-8')
        
        # Change the current working directory to the Git repository root path
        os.chdir(git_root_path)
        
        # Print the new working directory path
        print("Current working directory:", os.getcwd())
    except subprocess.CalledProcessError:
        print("Unable to retrieve Git repository root path.")
move_to_git_repo()

# COMMAND ----------

# MAGIC %sh
# MAGIC curl -s -H "Accept: application/vnd.github.VERSION.sha" \
# MAGIC   https://api.github.com/repos/snehasachu/test-repo/commits/main

# COMMAND ----------

# MAGIC %sh
# MAGIC curl -X GET \
# MAGIC   -H "Authorization: Bearer <token>" \
# MAGIC   -H "Content-Type: application/json" \
# MAGIC   -d '{
# MAGIC     "path": "/Workspace/Repos/sneha.ck@databricks.com/test-repo/test_notebook.py"
# MAGIC   }' \
# MAGIC   https://adb-6491134404419862.2.azuredatabricks.net/api/2.0/repos

# COMMAND ----------


