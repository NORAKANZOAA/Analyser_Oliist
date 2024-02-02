import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("training_dataset.csv")


st.set_page_config(page_title="Oliist Dataset")
st.header("Study of shipping revenues - Olist Dataset")
st.markdown("Explore the variables to understand their relationships .")
st.sidebar.header("Variable Comparison")


options = st.sidebar.radio("Select comparison",
                           options=[
                                    "price Vs score ",
                                    "temps_livraison Vs score",
                                    " retard_livraison Vs score"])

if options == "price Vs score":
    plot2 = px.bar(
    df,
    x="score",
    y="price",
    title="score vs price",
    )
elif options == "temps_livraison Vs score":
    plot3 = px.bar(
    df,
    x="Score",
    y="temps_livraison",
    title="temps livraison vs Petal score",
    )
elif options ==  " retard_livraison Vs score":
    plot4 = px.bar(
    df,
    x="score",
    y="retard_livraison",
    title="retard livraison vs score",
    )

st.plotly_chart(plot2)
st.plotly_chart(plot3)
st.plotly_chart(plot4)
