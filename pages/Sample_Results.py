import streamlit as st

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
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 40px; 
            color: #ff6200;'>
            Our Generated Results!
            </h1>
            """, unsafe_allow_html=True)

with sub_body1: 
    with sub_body1: 

        st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 20px; 
            color: #333333;'>
            A friendly orange lion in an office with 2 people
            </h1>
            """, unsafe_allow_html=True)

        show1, show2, show3 = st.columns(3)

        with show1:
            st.image('Imagen3/a friendly orange lion in an office with 2 people.jpg', use_column_width=True)

        with show2:
            st.image('Imagen3/a friendly orange lion in an office with 2 people1.jpg', use_column_width=True)
        
        with show3:
            st.image('Imagen3/a friendly orange lion in an office with 2 people2.jpg', use_column_width=True)


    with sub_body2: 

        st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 20px; 
            color: #333333;'>
            A group of 3 people in the office
            </h1>
            """, unsafe_allow_html=True)

        show4, show5 = st.columns(2)

        with show4:
            st.image('Imagen3/a group of three people in the office.jpg', use_column_width=True)

        with show5:
            st.image('Imagen3/a group of three people in the office2.jpg', use_column_width=True)
        

    with sub_body3: 

        st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 20px; 
            color: #333333;'>
            A woman and a friendly orange lion, doing the easy seat yoga pose
            </h1>
            """, unsafe_allow_html=True)

        show6, show7, show8 = st.columns(3)

        with show6:
            st.image('Imagen3/a woman and a friendly orange lion, doing the easy seat yoga pose.jpg', use_column_width=True)

        with show7:
            st.image('Imagen3/a woman and a friendly orange lion, doing the easy seat yoga pose2.jpg', use_column_width=True)
        
        with show8:
            st.image('Imagen3/a woman and a friendly orange lion, doing the easy seat yoga pose3.jpg', use_column_width=True)
    

    with sub_body4: 

        st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 20px; 
            color: #333333;'>
            A woman and a robot interacting
            </h1>
            """, unsafe_allow_html=True)

        show9, show10, show11 = st.columns(3)

        with show9:
            st.image('Imagen3/an image that shows a woman and a robot giving each other a high five.jpg', use_column_width=True)

        with show10:
            st.image('Imagen3/an image that shows a woman and a robot shaking hands.jpg', use_column_width=True)
        
        with show11:
            st.image('Imagen3/an image that shows a woman and a robot shaking hands1.jpg', use_column_width=True)
    

    with sub_body5: 

        st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 20px; 
            color: #333333;'>
            An orange lion in front of an office
            </h1>
            """, unsafe_allow_html=True)

        show12, show13 = st.columns(2)

        with show12:
            st.image('Imagen3/an orange lion in front of an office.jpg', use_column_width=True)

        with show13:
            st.image('Imagen3/an orange lion in front of an office2.jpg', use_column_width=True)
    

    with sub_body6: 

        st.markdown("""
            <h1 style='text-align: center; 
            font-family: Times New Roman; 
            font-size: 20px; 
            color: #333333;'>
            Two software developers giving each other a high five, wearing hoodies, energy drinks in the background, headphones around their neck
            </h1>
            """, unsafe_allow_html=True)

        show14, show15 = st.columns(2)

        with show14:
            st.image('Imagen3/two software developers giving each other a high five, wearing hoodies, energy drinks in the background, headphones around their neck.jpg', use_column_width=True)

        with show15:
            st.image('Imagen3/two software developers giving each other a high five, wearing ING hoodies, energy drinks in the background, headphones around their neck.jpg', use_column_width=True)
        
    

