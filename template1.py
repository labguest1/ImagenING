import streamlit as st
from PIL import Image

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


