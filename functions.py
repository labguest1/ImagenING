import streamlit as st

def autofill_option_1():
        st.session_state.input_text = '2 people shaking hands'
    
def autofill_option_2():
    st.session_state.input_text = 'A friendly lion dancing with people'

def generate_image():
    st.session_state.input_text = ""