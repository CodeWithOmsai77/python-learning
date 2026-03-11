# 6. Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv.

'''1. Open the Terminal: Navigate to your project folder and open the terminal window.

2. Generate the Requirements File: Run the command pip freeze > requirements.txt. This command captures all the packages and versions currently installed in your global system interpreter and saves them into a file named requirements.txt.

3. Create a New Virtual Environment: Use the virtualenv command followed by your chosen name to create the isolated environment, for example: virtualenv harryenv.

4. Activate the Environment: You must activate the newly created environment to work inside it. On Windows, use the activation script: .\harryenv\Scripts\activate.ps1. You will know it is active when the environment name appears in brackets in your terminal prompt.

5. Install Packages from the File: Replicate the system interpreter's setup by running pip install -r requirements.txt. This command automatically installs every module listed in the text file into your new virtual environment'''