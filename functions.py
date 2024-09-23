import streamlit as st
import streamlit.components.v1 as components


def autofill_option(text):
    st.session_state.input_text = text


def format_example_prompt_button(widget_label):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.color = 'black';
                    elements[i].style.background = 'transparent'
                    elements[i].style.border='none'
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)
