import streamlit as st
import json
from google.cloud import aiplatform
from google.oauth2 import service_account
import logging
import vertexai
from google.api_core.exceptions import GoogleAPICallError, RetryError, Forbidden


# def load_credentials(json_key_file):
#     with open(json_key_file) as f:
#         return json.load(f)


json_key_file = 'stream-5---fi-nonprod-svc-sgto-7b78037c37f6.json'
PROJECT_ID = '880058750453'
LOCATION = 'europe-west4'  

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


st.title("Vertex AI Connection Test")

if st.button("Test Connection"):
    try:
        # credentials_dict = load_credentials(json_key_file)
        # credentials = service_account.Credentials.from_service_account_info(credentials_dict)
        # aiplatform.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)
        # logger.info("Vertex AI initialized successfully.")

        vertexai.init(project=PROJECT_ID, location=LOCATION)
        logger.info("Vertex AI initialized successfully.")

        models = aiplatform.Model.list()
        logger.info(f"Retrieved models.")

        if models:
            st.success(f"Connection successful. Retrieved {len(models)} models")
        else:
            st.warning("No models found")

        st.success("Connection successful")


    except Forbidden as e:
        st.error(f"Permission denied: {str(e)}")

    except GoogleAPICallError as e:
        st.error(f"API call failed: {str(e)}")

    except RetryError as e:
        st.error(f"Retry failed: {str(e)}")

    except Exception as e:
        st.error(f"Connection failed: {str(e)}")
