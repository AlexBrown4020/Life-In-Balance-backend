# LifeInBalance
A web application for finding online yoga sessions and hosting them for clients

**Installation

1. Clone the repository from Github
2. You should have a virtual environment setup for your clone, but in case you dont, you can create one in the root directoy with: python -m venv .venv
3. Now you can activate the virtual environment with: . .venv.bin.activate OR . .venv.Scripts.activate
4. Make sure Django and DRF are installed within your venv: pip install django 
5. Once running, you should be able to run the migrations for your local machine: python manage.py migrate OR python3 manage.py migrate
6. 

** Potential Installation Issues:
* You may come across an error when installing django in your virtual environment: "Fatal error in launcher: Unable to create process using 'C:/users/...'
If so, try using the command: python -m pip install --upgrade pip  
This is to ensure the pip installation software is up to date.