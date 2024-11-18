import os
from dotenv import load_dotenv

load_dotenv('.env')

# Google Oauth 2.0 env
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REDIRECT_URI = os.environ['REDIRECT_URI']

# prova
SECRET_PROVA = os.environ['SECRET_PROVA']