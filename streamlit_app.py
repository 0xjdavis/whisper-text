import streamlit as st
from openai import OpenAI

openai_api_key = st.secrets["open_ai_key"]
client = OpenAI(api_key=openai_api_key)

audio_file = open("/path/to/file/speech.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

st.title("🎈 Whisper Text")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

print(transcription.text)
