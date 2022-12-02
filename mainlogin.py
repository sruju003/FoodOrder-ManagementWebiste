import streamlit as st
import base64
from app import main1
from customermain import main2

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/gif;base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('finalfood.gif') 

st.title("Gollas Food")
menu = ["Admin Login","Customer Login"]
choice = st.sidebar.selectbox("User Login", menu)
if choice=="Admin Login":
    form = st.form(key='my_form')
    username = form.text_input(label='Enter Admin Username')
    password = form.text_input('Enter Admin Password',type='password')
    submit_button = form.form_submit_button(label='Submit')
    if username=='foodAdmin' and password=='password':
        main1()


if choice=="Customer Login":
    form = st.form(key='my_form')
    username = form.text_input(label='Enter Customer Username')
    password = form.text_input(label='Enter Customer Password',type='password')
    submit_button = form.form_submit_button(label='Submit')
    if username=='C1' and password=='password':
        main2()











