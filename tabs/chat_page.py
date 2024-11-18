import streamlit as st
from utils.api import *
import json

def show_chat_page():
    st.title("Chat")
    
    messages = st.container()
    
    if prompt:=st.chat_input("Scrivi il messaggio..."):
        # messages.chat_message("user").write(prompt)
        
        try:
            answer = answer_message({ "text": "I'm providing some data that you have to associate FHIR resources. Here is the data:\n" + prompt })
            print("ANSWER\n", answer)
            # answer_json = json.dumps(json.loads(answer), ensure_ascii=False, indent=4)
            answer_json = json.dumps(answer, ensure_ascii=False, indent=4)
            
            # print("ANSWER JSON\n-------------\n"+ json.loads(answer) + "\n\n-------------------\n")
                    
            # if st.session_state.loading_template_fhir:
            #     messages.spinner("Caricamento risposta...")
                
            messages.chat_message("assistant").markdown(f"The data extracted is:\n ```json\n{answer_json}\n")
            st.session_state.loading_template = False
        except Exception as e:
            st.error("Internal server error")
            st.error(e)
        
        

show_chat_page()