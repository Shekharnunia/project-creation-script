## Command Line Script to create Project folder and make a repo on github and a local git repo

## Running the Script

First, clone the repository to your local machine:

```bash
git clone https://github.com/Shekharnunia/project-creation-script.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## Steps before initializing the source file
* Change the **cd /home/shekhar/Desktop/Development/** to your prefered project folder
* Give the address of your clone repo in this line to execute python file **python /home/shekhar/Desktop/Development/project-creation-script/project.py $1**
* Change the username in **git remote add origin https://github.com/Shekharnunia/$1.git** to your username
* Drivers : https://selenium-python.readthedocs.io/installation.html#drivers
* After downloading the apropriate drivers give relevant patht to **executable_path='/home/shekhar/chromedriver**


Initialise the Source file:

```bash
source ~/.project_command
```



Finally, run the command on terminal:

```bash
create folder-name
```
