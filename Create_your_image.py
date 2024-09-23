import streamlit as st
import json
from PIL import Image
import re
from io import BytesIO
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import time
from google.api_core.exceptions import ResourceExhausted
from streamlit_lottie import st_lottie_spinner, st_lottie
from functions import (
    autofill_option,
    format_example_prompt_button,
)

### project details ###
PROJECT_ID = "880058750453"
LOCATION = "europe-west4"
vertexai.init(project=PROJECT_ID, location=LOCATION)


### load imagen model ###
use_fast_model = True
model = "imagen-3.0-fast-generate-001" if use_fast_model else "imagen-3.0-generate-001"
generation_model = ImageGenerationModel.from_pretrained(model)


### page configuration ###
st.set_page_config(
    page_title="ImagenING",
    page_icon="ing_icon/tab_icon.jpg",
)


### load css style ###
with open("styles/styles_1.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


### define example propmts ###
example_prompt1 = "2 people shaking hands"
example_prompt2 = "A friendly orange lion shaking hands with people"
example_prompt3 = "People playing football with an orange lion"


### main page components ###
header = st.container()
body = st.container()
sub_body1 = st.container()
sub_body2 = st.container()
footer = st.container()

if 'count' not in st.session_state:
    with open("image_counter.txt", "r") as f:
        st.session_state.count = int(f.read())

if 'easter_egg' not in st.session_state:
    st.session_state.easter_egg = False


### main page header ###
with header:
    st.image("ing_icon/logo.svg", width=700)


### animations ###
path1 = "animations/spinner.json"
with open(path1, "r") as file:
    spinner_url = json.load(file)


### main page body ###
with body:
    if "input_text" not in st.session_state:
        st.session_state.input_text = ""

    user_prompt = st.text_input(
        r"$\textsf{\large Please enter your prompt}$",
        key="input_text",
        placeholder="type here",
    )

    if re.search(r'(?i)\bhappy\b\s+\blion\b', user_prompt):  
        st.session_state.easter_egg = True
    else: 
        st.session_state.easter_egg = False


    ### prompt option buttons ##
    prompt_button1, prompt_button2, prompt_button3 = st.columns(3)

    with prompt_button1:
        st.button(example_prompt1, on_click=autofill_option, args=[example_prompt1])
        format_example_prompt_button(example_prompt1)

    with prompt_button2:
        st.button(example_prompt2, on_click=autofill_option, args=[example_prompt2])
        format_example_prompt_button(example_prompt2)

    with prompt_button3:
        st.button(example_prompt3, on_click=autofill_option, args=[example_prompt3])
        format_example_prompt_button(example_prompt3)


    ## easter egg ## 
    lion_placeholder = st.empty()

    if st.session_state.easter_egg:
        lion_placeholder.markdown("🦁 **You found the secret lion!**")
        st.image("animations/dancing.gif", width=200)
    else:
        lion_placeholder.markdown("")


    ## settings option ##
    option = st.selectbox(
        r"$\textsf{\large Please select the setting}$",
        ["Office", "Customer", "Illustration"],
    )

    ## generate image button ##
    if st.button("Generate Image"):
        st.session_state.count += 4
        with open("image_counter.txt", "w") as f:
            f.write(str(st.session_state.count))
        with st_lottie_spinner(
            spinner_url,
            reverse=True,
            speed=1,
            loop=True,
            quality="high",
            height=130,
            width=130,
            key="spinner1",
        ):
            # pass
    
            if option == "Office":
                system_prompt = """
                                Setting:
                                diverse, happy, office setting, professional photography, high quality, colorful, energetic, orange elements, 
                                smiling, playful, funny situation, sustainable, fair society, harmony, team spirit, working together
                                Image Content:
                                """

            elif option == "Customer":
                system_prompt = """
                                Setting:
                                happy, fun, diverse, action, enjoying, natural, snapshot, daily life, energetic, playful, harmony, freedom
                                Image Content:
                                """

            elif option == "Illustration":
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
                        negative_prompt=negative_prompt,
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
                            st.image(
                                images[0], caption="Image 1", use_column_width=True
                            )

                        with img2:
                            st.image(
                                images[1], caption="Image 2", use_column_width=True
                            )

                    with sub_body2:
                        img3, img4 = st.columns(2)

                        with img3:
                            st.image(
                                images[2], caption="Image 3", use_column_width=True
                            )

                        with img4:
                            st.image(
                                images[3], caption="Image 4", use_column_width=True
                            )
                    
                    st.balloons()


with footer:
    st.markdown(
        f"""
        <div class="bottom-right">
            <p>Number of images generated today: {st.session_state.count}</p>
            <p>Total cost of images generated today: {f'{st.session_state.count * 0.16:.2f}'}€</p>
            <p>Cost per generated image: 0,16€</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
