import google.generativeai as genai
import os
#from dotenv import load_dotenv
import streamlit as st

#load_dotenv()

#gemini_api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key="AIzaSyDMvG66NCls_E-vARJuFZDwmECEeMGcSrw")
for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(f"names are {m.name} and temperature is {m.temperature}")

# Initialize Gemini-Pro 
model = genai.GenerativeModel('gemini-1.5-flash')

# Add a Gemini Chat history object to Streamlit session state
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history = [])

#Title for ChatBot Application
st.title("Ngobrol dengan Haraki-bot")
st.write("powered by Google Gemini-Pro AI Model")


# Display prompt messages history
for message in st.session_state.chat.history:
    with st.chat_message("ai"):
        st.markdown(message.parts[0].text)

default_prompt = "Sebagai seorang ahli pendidikan, saya siap membantu Anda. Apa yang ingin Anda tanyakan?"
prompt = st.chat_input(default_prompt)


if prompt:
  st.chat_message("user").markdown(prompt)
  #Pass User Prompt/Message to Gemini Model and get response
  response = st.session_state.chat.send_message(prompt)

  with st.chat_message("ai"):
     st.markdown(response.text)
  #st.write(response['answer'])
