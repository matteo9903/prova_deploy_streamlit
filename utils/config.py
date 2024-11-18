import os
from dotenv import load_dotenv

load_dotenv('.env')

import streamlit as st

# Google Oauth 2.0 env
CLIENT_ID = st.secrets("CLIENT_ID")
CLIENT_SECRET = st.secrets("CLIENT_SECRET")
REDIRECT_URI = st.secrets("REDIRECT_URI")

# prova
SECRET_PROVA = st.secrets("SECRET_PROVA")