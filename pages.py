import streamlit as st 
import pandas as pd


class Pages:
    def intro_page():
        st.title("This is the Intro Page")

    def main_page():
        st.title("This is Main")
    
    def body_page():
        st.title("Here is the dataset")
    
    def closing_page():
        st.title("This is the Closing page")
        
class Data:
    def load_data():
        df = pd.read_csv('dataset.csv', encoding='ISO-8859-1')
        return df
