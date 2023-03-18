import streamlit as st
from pages import Pages
from pages import Data
# from pages.py import Class Pages and the functions under it

list_of_pages = [
    "Intro",
    "Main", 
    "Body", 
    "Closing"
    ]
    
st.sidebar.title(':scroll: Main Pages')
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Intro":
    Pages.intro_page()

elif selection == "Main":
    Pages.main_page()

elif selection == "Body":
    Pages.body_page()
    
elif selection == "Closing":
    Pages.closing_page()