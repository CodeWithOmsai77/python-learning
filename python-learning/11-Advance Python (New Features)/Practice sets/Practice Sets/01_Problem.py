'''
1. Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?
->

1. Install the virtualenv package: Begin by installing the virtualenv module globally using the command pip install virtualenv.

2. Create the environments: Generate two distinct virtual environments by running the commands virtualenv env1 and virtualenv env2 in your terminal.

3. Activate the first environment: To start working in the first environment, you must activate it. Harry demonstrates this by navigating to the scripts folder and running the activation file (e.g., .\env1\Scripts\activate.ps1 on Windows).

4. Install packages in the first environment: Once env1 is active, install the specified packages, such as pandas and pyjoke, using the pip install command.

5. Generate a requirements.txt file: Use the command pip freeze > requirements.txt while the first environment is still active. This lists all installed packages and their versions in a single text file.

6. Switch environments: Deactivate the first environment by simply typing deactivate. Then, activate the second environment (env2) using its respective activation script.

7. Install packages in the second environment: To replicate the setup from the first environment, run the command pip install -r requirements.txt. This automatically installs all modules listed in the requirements file into the second virtual environment
'''