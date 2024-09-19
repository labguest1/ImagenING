import streamlit as st
from PIL import Image
from io import BytesIO
import json
from google.cloud import aiplatform
from google.oauth2 import service_account
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time
from google.api_core.exceptions import ResourceExhausted


# credentials
# def load_credentials(json_key_file):
#     with open(json_key_file) as f:
#         return json.load(f)

PROJECT_ID = '880058750453'
LOCATION = 'europe-west4'  
json_key_file = 'stream-5---fi-nonprod-svc-sgto-7b78037c37f6.json'

# credentials_dict = load_credentials(json_key_file)

# credentials = service_account.Credentials.from_service_account_info(credentials_dict)
# aiplatform.init(project=PROJECT_ID, location=LOCATION, credentials=credentials)
vertexai.init(project=PROJECT_ID, location=LOCATION)

# model
use_fast_model = True 
model = "imagen-3.0-fast-generate-001" if use_fast_model else "imagen-3.0-generate-001"
generation_model = ImageGenerationModel.from_pretrained(model)


# components
header = st.container()
body = st.container()


# header
with header: 
    st.markdown("""
            <h1 style='text-align: center; 
            font-family: Sans-Serif; 
            font-size: 30px; 
            color: #ff6200;'>
            The BEST Image Generator EVER
            </h1>
            """, unsafe_allow_html=True)

    st.image('imagin.png')


# body
with body: 
    user_prompt = st.text_input('Please type in your prompt')
    option = st.selectbox('Please select the setting', ['Office', 'Outdoors'])

    if st.button('Generate Image'):
        if option == 'Office':
            system_prompt = """
                            Setting:
                            diverse, happy, office setting, professional photography, high quality, colorful, energetic, orange elements, smiling, playful, funny situation, sustainable, fair society, harmony, team spirit, working together
                            Image Content:
                            """
        
        
        elif option == 'Outdoors':
            system_prompt = """
                            Setting:
                            diverse, happy, outdoor setting, professional photography, high quality, colorful, energetic, orange elements, smiling, playful, funny situation, sustainable, fair society, harmony, team spirit, working together
                            Image Content:
                            """

        negative_prompt = """
            out of frame, lowres, text, cropped, worst quality, low quality, jpeg artifacts, duplicate, mutilated, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, bad anatomy, bad proportions, extra limbs, cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, fused fingers, too many fingers, long neck, watermark, signature, brands, violence, weapons, blood
            """
        
        prompt = system_prompt + user_prompt

        success = False

        while not success:
            try:
                response = generation_model.generate_images(
                    prompt=prompt,
                    number_of_images=4,
                    aspect_ratio="4:3",
                    safety_filter_level="block_some",
                    person_generation="allow_adult", 
                    negative_prompt=negative_prompt
                )

            except ResourceExhausted:
                print("Resource is exhausted, trying again in 2 seconds")
                time.sleep(2)

            except Exception as e:
                st.error(f"Error generating image: {e}")

            else:
                success = True

                images = []

                for index in range(len(list(response))):
                    image_data = response.images[index]._image_bytes
                    image = Image.open(BytesIO(image_data))
                    images.append(image)

                img1, img2, img3, img4 = st.columns(4)
                
                with img1:
                    st.image(images[0], caption='Image 1', use_column_width=True)
                
                with img2:
                    st.image(images[1], caption='Image 2', use_column_width=True)

                with img3:
                    st.image(images[2], caption='Image 3', use_column_width=True)

                with img4:
                    st.image(images[3], caption='Image 4', use_column_width=True)

                







