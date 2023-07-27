import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns([0.2, 0.7])

with col1:
    st.image("images/me.jpg", use_column_width=True)

with col2:
    st.title("Eglė Babachinaitė")
    content = """
    I am a Python enthusiast with a heart that beats for crafting elegant and efficient solutions 
    through programming. Python, to me, is more than just a language; it's an art form that empowers 
    me to bring ideas to life and make the impossible, possible. 
    
    As I seek to embark on my journey as a Python developer, I don't merely want to stand out; I 
    strive to illuminate the way for innovation and excellence. My projects are a testament to my 
    commitment to continuous growth and learning. I am ready to embrace challenges, collaborate with 
    like-minded visionaries, and make a significant impact in the Python-powered world. 
    
    Currently, I find myself weaving the strands of imagination into reality as I create a 
    mesmerizing Unicorn plush toys e-shop with Django. Combining my love for Python with the power 
    of Django, I aim to create an enchanting user experience where the magic of technology meets 
    the charm of creativity.
    
    With every line of code, I delve into a world of limitless possibilities, and my journey has 
    been adorned with captivating projects that reflect my dedication.  
    """
    st.info(content)

content2 = """
Below you can find projects I have built in Python. Let's embark on this incredible journey 
together, driven by innovation and empowered by the magic of Python.
"""
st.write(content2)

# columns with ratio dimensions
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:9].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[9:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
