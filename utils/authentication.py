import requests
import streamlit as st

from utils.config import *


def verify_token():
    query_params = st.query_params
    if "code" in query_params:
        code_values = query_params.get("code")
        return code_values
    return None


def google_auth():
    token = verify_token()
    if token is not None:
        verify_token_url = "https://oauth2.googleapis.com/token"
        payload = {
            "code": token,
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "authorization_code",
            "redirect_uri": REDIRECT_URI,
        }

        response = requests.post(verify_token_url, data=payload)

        return response
