# medi_assessment

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