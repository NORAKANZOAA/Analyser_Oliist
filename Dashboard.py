import streamlit as st
import pandas as pd


# set up training_dataset
df = pd.read_csv("training_dataset.csv")

# make page

st.set_page_config(page_title="Olist Dataset")
st.header("Olist Machine Learning Project")
st.markdown("Deployment of the Olist dataset machine learning model using LogesticRegression.")
st.markdown("Use this dashboard to understand the data and to make predictions.")
st.markdown("")
st.image("ecommerce-brazil.jpg")


