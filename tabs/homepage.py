import streamlit as st
from utils.config import *

@st.cache_data(show_spinner=False)
def show_home_page():
    
    with st.container():
        welcome = st.container()
        welcome.title(SECRET_PROVA)
        col1, col2 = welcome.columns([0.6, 0.4])
        with col1:
            st.header("Ciao! Sono il tuo assistente sanitario basato su Intelligenza Artificiale. "
                      "Sono qui per aiutarti a mappare i tuoi dati in risorse FHIR e OMOP."
                      )
            st.divider()
            st.subheader(
                "Con me puoi generare risorse per garantire il miglioramento dell'efficienza dell'interoperabilità tra dati sanitari."
            )
        with col2:
            st.image("./assets/ai_image.jpeg", use_column_width=True)

        
    footer = st.container()
    with footer:
        mission, info, contact = footer.columns((2, 1, 1))
        with mission:
            mission.header("Mission")
            mission.markdown("""<p>Il progetto mira ad <strong>automatizzare</strong> la <strong>traduzione</strong> di 
            <strong>dati tabellari</strong> negli standard <strong>FHIR</strong> e <strong>OMOP</strong>, mediante l'utilizzo dei Large Language Models (LLM).
            A causa della diversità dei formati utilizzati dai vari sistemi sanitari per archiviare i dati, la traduzione 
            di tali informazioni in risorse standardizzate è fondamentale. Questo processo non solo favorisce 
            lo scambio e l'accesso universale ai dati, ma adotta un formato standard riconosciuto a livello internazionale, 
            contribuendo all'efficienza e all'interoperabilità dei <strong>sistemi informativi sanitari</strong>.</p>""",
                                unsafe_allow_html=True)

        with info:
            info.header("Disclaimer")
            info.markdown("""<p><em>HBD-LLM è in fase di preview e potrebbe commettere errori. Analizza le risposte e 
            verificane la correttezza.</em></p>""", unsafe_allow_html=True)

        with contact:
            contact.header("Contacts")
            contact.markdown(
                '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.0/css/all.min.css"/>',
                unsafe_allow_html=True)
            contact.markdown("""
            <i class="fa-solid fa-house"></i><a href="https://www.ieo.it/" target="_blank"> www.ieo.it</a><br>
            <i class="fa-solid fa-location-dot"></i> Via Ripamonti 435, I-20132 Milano<br>
            <a href="https://www.facebook.com/IstitutoEuropeoDiOncologia" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            <a href="https://www.instagram.com/ieoistitutoeuropeodioncologia?igshid=YTQwZjQ0NmI0OA==" target="_blank"><i class="fa-brands fa-instagram" style="margin-left: 20px;"></i></a>
            <a href="https://www.linkedin.com/company/ieo-istituto-europeo-di-oncologia/" target="_blank"><i class="fa-brands fa-linkedin" style="margin-left: 20px;"></i></a><br>
            <i class="fa-solid fa-house"></i><a href="https://www.reply.com/laife-reply/en/" target="_blank"> www.reply.com</a><br>
            <i class="fa-solid fa-location-dot"></i> Via Bensi 1/2, 20152 Milano<br>
            <a href="https://www.facebook.com/laife.reply" target="_blank"><i class="fa-brands fa-facebook"></i></a>
            <a href="https://www.instagram.com/laife.reply?igshid=YTQwZjQ0NmI0OA==" target="_blank"><i class="fa-brands fa-instagram" style="margin-left: 20px;"></i></a>
            <a href="https://www.linkedin.com/company/laife-reply/" target="_blank"><i class="fa-brands fa-linkedin" style="margin-left: 20px;"></i></a>
            """, unsafe_allow_html=True)

    footer.divider()
    
    
show_home_page()