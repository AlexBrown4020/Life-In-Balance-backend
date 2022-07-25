# LifeInBalance
A web application for finding online yoga sessions and hosting them for clients

**Installation

1. Clone the repository from Github
2. You should have a virtual environment setup for your clone, but in case you dont, you can create one in the root directoy with: python -m venv .venv
3. Now you can activate the virtual environment with: . .venv.bin.activate OR . .venv.Scripts.activate
4. Make sure Django and DRF are installed within your venv: pip install django 
5. Once running, you should be able to run the migrations for your local machine: python manage.py migrate OR python3 manage.py migrate

**Heroku Deployment
Since Life in Balance is intended to be a RESTful API with a separated frontend, we will need to deploy the backend to allow calls to be made.  In this example we will be using a Heroku server, but feel free to use any that work for you.

1. Before continuing, check you are still in your virtual enviroment.Run: python install gunicorn
  - Gunicorn is necessary for web server gateway interface
2. Run: pip freeze > requirements.txt
  - This is to create a txt document containing all of the necessary tools for Heroku to make use of.
  - Make sure this is created in your projects root folder.
3. Create in the same place as requirements.txt: runtime.txt
  - This will keep a record of the current version of Python you are using, make sure to write inside it the version you have installed like this: python-3.9.5
4. Heroku requries a postgreSQL database to be deployed, so we will next make some modifications to settings.py in our first application
At the top of the page:
 - import dj_database_url
 - import django_heroku
Next, change debug to be false instead of true. You can also specify which host you want to allow access, but in this case we are using '*' to allow all.
 - DEBUG = False
 - ALLOWED_HOSTS = ['*']
Within the MIDDLEWARE array, include these two dependencies:
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
Also we have to change our default database from sqlite3 to postgreSQL, find DATABASES
  - replace sqlite3 with 'postgresql_psycopg2'
  - replace NAME to be: BASE_DIR / 'ciba',
Add to your static_files section:
  - STATIC_ROOT = BASE_DIR / 'static'
  - STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
Finally, add this to the bottom of the page to let Heroku know to use your local settings:
  - django_heroku.settings(locals())

5. Now your backend should be ready to deploy, follow instructions on Heroku to create your server and connect this backend.  I recommend linking it to your cloned repository so that it automatically updates the server.
https://devcenter.heroku.com/articles/git

** Potential Installation Issues:
* You may come across an error when installing django in your virtual environment: "Fatal error in launcher: Unable to create process using 'C:/users/...'
If so, try using the command: python -m pip install --upgrade pip  
This is to ensure the pip installation software is up to date.
