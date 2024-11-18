import streamlit as st

from utils.config import *
from utils.authentication import google_auth

def show_login_page():
    auth_url = "https://accounts.google.com/o/oauth2/auth"
    scope = "https://www.googleapis.com/auth/userinfo.email"
    auth_endpoint = f"{auth_url}?client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope={scope}&response_type=code"
    
    
    _, login_col, _ = st.columns([0.2, 0.6, 0.2])
    login_container = login_col.container(border=True)
    with login_container:
        st.title("Login")
        col1, col2 = st.columns(2)
        col1.write("Benvenuto nella nostra WebApp! Attraverso la potenza della Generative AI e dei Large Language Models, "
                   "possiamo trasformare i tuoi dati in risorse FHIR e OMOP come mai prima d'ora. Entra nel nostro mondo "
                   "di innovazione e collaborazione, dove la tua salute è al centro di tutto ciò che facciamo.")
        col2.image("./assets/ieo.png", use_column_width=True)
        
        button = st.button("LOGIN")
        if button:
            st.session_state.logged = True
    
        # st.markdown(
        #         f"""
        #         <p align="center">
        #             <a href="{auth_endpoint}" target="_self">
        #                 <img src="https://developers.google.com/identity/images/btn_google_signin_light_normal_web.png" 
        #                 alt="Login with Google">
        #             </a>
        #         </p>
        #         <p><br></p>
        #         """,
        #         unsafe_allow_html=True
        #     )
        
        # response = google_auth()
        # print("***Response: ", response)
        # if response is not None and 'error' not in response.json():
        #     response_data = response.json()
        #     print("***Response data: ", response_data)
        #     if response.status_code == 200:
        #         st.session_state.logged = True
        #         st.rerun()