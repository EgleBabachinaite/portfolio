import streamlit as st

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.image("images/skillup_certificate.png", width=800)
st.image("images/udemy_certificate.png", width=800)
st.image("images/javascript_certificate.jpg", width=800)
