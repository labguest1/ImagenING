import streamlit as st
import json
from PIL import Image
from io import BytesIO
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time
from google.api_core.exceptions import ResourceExhausted
from streamlit_lottie import st_lottie_spinner, st_lottie
from functions import autofill_option_1, autofill_option_2


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
    st.image('ing_icon/imagin.png', width=700)


### animations ### 
path1 = "animations/spinner.json"
with open(path1,"r") as file: 
    spinner_url = json.load(file) 

path2 = "animations/confetti.json"
with open(path2,"r") as file2: 
    confetti_url = json.load(file2) 


### customize button ###
st.markdown("""
    <style>
    div.stButton > button {
        background-color: white;
        color: #ff6200;
        height: 3em;
        width: 11em;
        border-radius:10px;
        border: 1px solid #ff6200;
        font-size: 20px;
        font-weight: bold;
    }
    div.stButton > button:hover {
        background-color: #ff6200;
        color: white;
        border: 1px solid #ff6200;
    }
    div.stButton > button:active {
        background-color: white;
        color: #ff6200;
        border: 1px solid #ff6200;
    }
    </style>
    """, unsafe_allow_html=True)


### main page body ###
with body: 
    if 'input_text' not in st.session_state:
        st.session_state.input_text =""

    user_prompt = st.text_input('Please type in your prompt', key='input_text')
    
    prompt_button1, prompt_button2 = st.columns(2)

    with prompt_button1:
        st.button('2 people shaking hands', on_click=autofill_option_1)
    
    with prompt_button2:
        st.button('A friendly orange lion shaking hands with people', on_click=autofill_option_2)
   
    option = st.selectbox('Please select the setting', ['Office', 'Customer', 'Illustration'])

    if st.button('Generate Image'):
        with st_lottie_spinner(spinner_url, reverse=True, speed=1, loop=True, quality='high', height=130, width=130, key='spinner1'):
            if option == 'Office':
                system_prompt = """
                                Setting:
                                diverse, happy, office setting, professional photography, high quality, colorful, energetic, orange elements, 
                                smiling, playful, funny situation, sustainable, fair society, harmony, team spirit, working together
                                Image Content:
                                """
            
            elif option == 'Customer':
                system_prompt = """
                                Setting:
                                happy, fun, diverse, action, enjoying, natural, snapshot, daily life, energetic, playful, harmony, freedom
                                Image Content:
                                """

            elif option == 'Illustration':
                system_prompt = """
                                Setting:
                                flat design illustraton, minimalistic, simple geometric shapes, happy, fun, diverse, simple, smooth rounded edges,
                                non-realistic, no complex details on texture, white background
                                Image Content:
                                """

            negative_prompt = """
                out of frame, lowres, text, cropped, worst quality, low quality, jpeg artifacts, duplicate, mutilated, extra fingers, 
                mutated hands, poorly drawn hands, poorly drawn face, mutation, deformed, blurry, bad anatomy, bad proportions, extra limbs, 
                cloned face, disfigured, gross proportions, malformed limbs, missing arms, missing legs, extra arms, extra legs, 
                fused fingers, too many fingers, long neck, watermark, signature, brands, violence, weapons, blood, nudity
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

                    st_lottie(confetti_url, reverse=True, speed=1, loop=False,
                                           quality='high', height=200, width=200, key='confetti1')







