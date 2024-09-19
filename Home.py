import streamlit as st
from PIL import Image
from io import BytesIO
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time
from google.api_core.exceptions import ResourceExhausted


### project details ###
PROJECT_ID = '880058750453'
LOCATION = 'europe-west4'  

vertexai.init(project=PROJECT_ID, location=LOCATION)


### load imagen model ###
use_fast_model = True 
model = "imagen-3.0-fast-generate-001" if use_fast_model else "imagen-3.0-generate-001"
generation_model = ImageGenerationModel.from_pretrained(model)


### app page icon ###
st.set_page_config(
    page_title="ImagING",
    page_icon="ing_icon/tab_icon.jpg",
)

### main page components ###
header = st.container()
body = st.container()
sub_body1 = st.container()
sub_body2 = st.container()


### main page header ###
with header: 
    st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 35px; 
            color: #ff6200;'>
            The BEST Image Generator EVER
            </h1>
            """, unsafe_allow_html=True)

    st.image('ing_icon/imagin.png', width=600)

### button customize ###
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #ff6200;
        color: white;
        height: 2em;
        width: 6em;
        border-radius:10px;
        border:1px solid #ff6200;
        font-size: 25px;
        font-weight: bold;
    }
    div.stButton > button:first-child:hover {
        background-color: #ff8533;
        color: white;
        border:1px solid #ff8533;
    }
    </style>
    """, unsafe_allow_html=True)


### main page body ###
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

                with sub_body1: 
                    img1, img2 = st.columns(2)
                
                    with img1:
                        st.image(images[0], caption='Image 1', use_column_width=True)
                    
                    with img2:
                        st.image(images[1], caption='Image 2', use_column_width=True)

                with sub_body2: 
                    img3, img4 = st.columns(2)

                    with img3:
                        st.image(images[2], caption='Image 3', use_column_width=True)

                    with img4:
                        st.image(images[3], caption='Image 4', use_column_width=True)

                







