import streamlit as st

from utils.config import *


from tabs.login import show_login_page


def init_state():
    if 'logged' not in st.session_state:
        st.session_state.logged = False
    if 'loading_template_fhir' not in st.session_state:
        st.session_state.loading_template_fhir = True


def main():
    init_state()
        
    if st.session_state.logged:
        # nascondere pulsante per ingrandire immagine
        hide_img_fs = '''
                <style>
                button[title="View fullscreen"]{
                    visibility: hidden;}
                </style>
                '''

        st.markdown(hide_img_fs, unsafe_allow_html=True)
        
        pg = st.navigation([
                        st.Page("tabs/homepage.py", title="Home", url_path='', default=True, icon=':material/home:'), 
                        st.Page("tabs/chat_page.py", title="Chat", url_path='chat', icon=':material/chat:'), 
                        ])
        pg.run()
        
        with st.sidebar:
            st.image("./assets/laife.png", use_column_width=True)
            st.divider()
            st.image("./assets/ieo.png", use_column_width=True)

    else:
        show_login_page()


st.set_page_config(
        page_title="HBD-LLM App",
        page_icon="./assets/favicon.png",
        layout="wide",
    )

main()