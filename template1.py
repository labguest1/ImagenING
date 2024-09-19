import streamlit as st
from PIL import Image

# heading
st.markdown("""
            <h1 style='text-align: center; 
            font-family: Sans-Serif; 
            font-size: 30px; 
            color: #fa551e;'>
            The BEST Image Generator EVER
            </h1>
            """, unsafe_allow_html=True)


st.image('imagin.png', width=700)


# body
user_prompt = st.text_input('Please type in your prompt')
option = st.selectbox('Please select the setting', ['Office', 'Outdoors'])


# footer
if st.button('Generate Image'):
    if option == 'Office':
        result_image = Image.open('sample/sample1.jpg')
        st.image(result_image, caption='image1',use_column_width=True)
    
    elif option == 'Outdoors':
        result_image = Image.open('sample/sample2.png')
        st.image(result_image, caption='image1',use_column_width=True)

    else:
        st.write('Please choose a setting')


