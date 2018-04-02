# Sample full stack Django application for a backend Python position at Medi Weightloss.

## All image files, product names, and product descriptions are the property of Medi Weightloss Inc. and are used purely for demonstration purposes of the assessment.

# View the project [Live Link](https://medi-shop-198920.appspot.com/)
- Deployed on Google Cloud (Flexible App Engine container) using Gunicorn WSGI server.
- Database is a Google Cloud Postgres instance.
- Static files served securely from a Google Cloud bucket.
- I also learned how to deploy the Django project to Google Cloud's Fleixble App Engine and wrote a [complete guide](https://medium.com/@vampiire/beginners-guide-to-deploying-a-django-postgresql-project-on-google-cloud-s-flexible-app-engine-e3357b601b91) on the process

# Steps for local testing (requires Conda for environment management)

## Clone the project
- `$ git clone https://github.com/the-vampiire/medi_assessment`
- cd into the project directory

## Conda Environment Configuration
- create a new environment: `$ conda create -n medi_patrick python=3.6 django psycopg2`
- create the activate / deactivate script directories for the conda env: `$ mkdir -p ~/anaconda3/envs/medi_patrick/etc/conda/activate.d; mkdir -p ~/anaconda3/envs/medi_patrick/etc/conda/deactivate.d`
- create and open a bash script that will export the environment variables when the environment is activated: `$ vim ~/anaconda3/envs/medi_patrick/etc/conda/activate.d/env_vars.sh` 
- paste the environment variables attached in the email into the now open VIM editor.
- save and close the file by pressing `esc` key then the `:` key followed by the `x` and `enter` keys
- create and open a bash script that will deactivate the environment variables when the environment is deactivated: `$ vim ~/anaconda3/envs/medi_patrick/etc/conda/deactivate.d/env_vars.sh`
- paste in the following line `unset SECRET_KEY DB_NAME DB_USER DB_PASSWORD DB_HOST DB_PORT`
- save and close the file by pressing `esc` key then the `:` key followed by the `x` and `enter` keys

# Project Startup
- activate the environment `conda activate medi_patrick`
- start the test server `./manage.py runserver`
- navigate to `localhost:8000/`
