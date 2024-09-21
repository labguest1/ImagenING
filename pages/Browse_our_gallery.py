import streamlit as st
from streamlit_carousel import carousel


### page configuration ###
st.set_page_config(
    page_title="ImagenING",
    page_icon="ing_icon/tab_icon.jpg",
)

### load css style ###
with open('styles/styles_2.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


### page components ###
header = st.container()
sub_body1 = st.container()
sub_body2 = st.container()
sub_body3 = st.container()
sub_body4 = st.container()
sub_body5 = st.container()
sub_body6 = st.container()


### page header ###
with header: 
    st.markdown("""
                <h1>
                Our Generated Results!
                </h1>
                """, unsafe_allow_html=True)

with sub_body1:
    st.markdown("""
                <h2>
                A friendly orange lion in an office with 2 people
                </h2>
                """, unsafe_allow_html=True)
    
    carousel1 = [
            dict(
                title="",
                text="",
                img='Imagen3/a friendly orange lion in an office with 2 people.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/a friendly orange lion in an office with 2 people1.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/a friendly orange lion in an office with 2 people2.jpg',
            )
            ]
    
    carousel(items=carousel1)


with sub_body2: 
    st.markdown("""
        <h2>
        A group of 3 people in the office
        </h2>
        """, unsafe_allow_html=True)

    carousel2 = [
            dict(
                title="",
                text="",
                img='Imagen3/a group of three people in the office.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/a group of three people in the office2.jpg',
            )
            ]

    carousel(items=carousel2)


with sub_body3: 
    st.markdown("""
        <h2>
        A woman and a friendly orange lion, doing the easy seat yoga pose
        </h2>
        """, unsafe_allow_html=True)

    carousel3 = [
            dict(
                title="",
                text="",
                img='Imagen3/a woman and a friendly orange lion, doing the easy seat yoga pose.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/a woman and a friendly orange lion, doing the easy seat yoga pose2.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/a woman and a friendly orange lion, doing the easy seat yoga pose3.jpg',
            )
            ]

    carousel(items=carousel3)


with sub_body4: 

    st.markdown("""
        <h2>
        A woman and a robot interacting
        </h2>
        """, unsafe_allow_html=True)

    carousel4 = [
            dict(
                title="",
                text="",
                img='Imagen3/an image that shows a woman and a robot giving each other a high five.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/an image that shows a woman and a robot shaking hands.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/an image that shows a woman and a robot shaking hands1.jpg',
            )
            ]

    carousel(items=carousel4)


with sub_body5: 
    st.markdown("""
        <h2>
        An orange lion in front of an office
        </h2>
        """, unsafe_allow_html=True)

    carousel5 = [
            dict(
                title="",
                text="",
                img='Imagen3/an orange lion in front of an office.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/an orange lion in front of an office2.jpg',
            )
            ]

    carousel(items=carousel5)


with sub_body6: 

    st.markdown("""
        <h2>
        Two software developers giving each other a high five, wearing hoodies, energy drinks in the background, headphones around their neck
        </h2>
        """, unsafe_allow_html=True)

    carousel6 = [
            dict(
                title="",
                text="",
                img='Imagen3/two software developers giving each other a high five, wearing hoodies, energy drinks in the background, headphones around their neck.jpg',
            ),
            dict(
                title="",
                text="",
                img='Imagen3/two software developers giving each other a high five, wearing ING hoodies, energy drinks in the background, headphones around their neck.jpg',
            )
            ]

    carousel(items=carousel6)

    
    