import streamlit as st
from PIL import Image
import json
from google.cloud import aiplatform
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time
from google.api_core.exceptions import ResourceExhausted


def load_credentials(json_key_file):
    with open(json_key_file) as f:
        return json.load(f)

PROJECT_ID = '880058750453'
LOCATION = 'europe-west4'  
json_key_file = 'C:/Users/CassandraSoongWeiran/Desktop/Project1/stream-5---fi-nonprod-svc-sgto-7b78037c37f6.json'

credentials = load_credentials(json_key_file)
vertexai.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)

# heading
st.markdown("<h1 style='text-align: center'>The BEST Image Generator EVER</h1>", unsafe_allow_html=True)
st.image('C:/Users/CassandraSoongWeiran/Desktop/Project1/imagin.png')

# body
user_prompt = st.text_input('Please type in your prompt')
option = st.selectbox('Please select the setting', ['Office', 'Outdoors'])

# footer
if st.button('Generate Image'):
    if option == 'Office':
        result_image = Image.open('C:/Users/CassandraSoongWeiran/Desktop/Project1/sample1.jpg')
        st.image(result_image, caption='result',use_column_width=True)
    
    elif option == 'Outdoors':
        result_image = Image.open('C:/Users/CassandraSoongWeiran/Desktop/Project1/sample2.png')
        st.image(result_image, caption='result',use_column_width=True)

    else:
        st.write('Please choose a setting')


    #     # Call the Imagen model for image generation
    #     try:
    #         response = vertexai.image_generation.generate_image(prompt=prompt)
    #         image_url = response.image_url

    #         # Display the generated image
    #         st.image(image_url, caption="Generated Image", use_column_width=True)
    #     except Exception as e:
    #         st.error(f"Error generating image: {e}")
    # else:
    #     st.warning("Please enter a description.")






