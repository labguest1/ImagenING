import streamlit as st
import json
from google.cloud import aiplatform
from google.oauth2 import service_account
import vertexai

def load_credentials(json_key_file):
    with open(json_key_file) as f:
        return json.load(f)

json_key_file = 'C:/Users/CassandraSoongWeiran/Desktop/Project1/stream-5---fi-nonprod-svc-sgto-7b78037c37f6.json'
PROJECT_ID = '880058750453'
LOCATION = 'europe-west4'  

st.title("Vertex AI Connection Test")

if st.button("Test Connection"):
    try:
        credentials_dict = load_credentials(json_key_file)
        credentials = service_account.Credentials.from_service_account_info(credentials_dict)
        aiplatform.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

        project_info = aiplatform.Project(project=PROJECT_ID)
        st.success("Connection successful")

    except Exception as e:
        st.error(f"Connection failed: {str(e)}")
