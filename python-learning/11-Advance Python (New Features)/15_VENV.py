# Steps to create the virtual environement 
'''
1. Install the virtualenv package: First, you must install the virtualenv module globally using the command pip install virtualenv.

2. Create the environment: In your terminal, run the command virtualenv env_name (replacing env_name with your preferred name, such as env or myenv). This generates a folder containing an isolated Python interpreter.

3. Activate the environment: You must activate the environment to start using it. On Windows, navigate to the scripts folder and run the activation file using the command .\env_name\Scripts\activate.ps1. When successful, the name of the environment will appear in brackets in your terminal prompt.

4. Install isolated packages: While the virtual environment is active, you can install specific versions of packages (for example, pip install pandas) without affecting your global Python installation.

5. Deactivate the environment: To exit the isolated environment and return to the global system interpreter, simply type the command deactivate.

Harry explains that these steps are vital for isolating dependencies and preventing conflicts between different package versions required by different projects. Additionally, he suggests using pip freeze > requirements.txt once your environment is set up so that you can easily recreate the exact same setup later by running pip install -r requirements.txt
'''