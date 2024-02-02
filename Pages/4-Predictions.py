import streamlit as st
import numpy as np
from make_pred import make_prediction
import json
import pandas as pd
import plotly.express as px
import requests
from sklearn.metrics import recall_score, accuracy_score, f1_score

df = pd.read_csv("training_dataset.csv")

st.set_page_config(page_title="Prediction")
st.header("Prediction - Olist Dataset")
st.markdown("Utilize the LogisticRegression to display a score of  Olist_Machine learning Model.")
            
st.sidebar.header("Make Prediction")

freight_value = st.sidebar.text_input("freight value")
price = st.sidebar.text_input("price")
make_pred_API = st.sidebar.button("Predict")


plot1 = px.scatter(
    df,
    x="price",
    y="freight_value",
    title="freight_value vs price",
    )









if make_pred_API:
    # Construire l'URL avec les paramètres
    url = f"http://localhost:8000/{float(freight_value)}/{float(price)}"

    # Envoyer la requête à FastAPI
    response = requests.get(url)

    # Vérifier si la requête a réussi (statut 200)
    if response.status_code == 200:
        score_pred = response.json()["prediction"]
        st.success(f"Prediction result: {score_pred} ")
        
    #     st.success((f"Pour le jeu d'entrainement: \n le recall est de {recall_train}, \n l'accuracy de {acc_train} \n le f1 score de {f1_train}"))
    #     st.success(f"Pour le jeu de test: \n le recall est de {recall_test}, \n l'accuracy de {acc_test} \n le f1 score de {f1_test}")
    # else:
        st.error("Error in prediction request.")

    # Transformer mes x1/x2/x3/x4 en df
    p1 = [float(freight_value), float(price)]
    x = np.array([p1])
    row = {"freight value": [float(freight_value)],
           "price": [float(price)]}

    p1_df = pd.DataFrame(row)

    # plot1.add_scatter(x=p1_df["freight_value"], 
    #                   y=p1_df["price"],
    #                   mode='markers',  
    #                   name=score_pred,  
    #                   marker=dict(
    #                         color='red',  # Couleur des points
    #                         size=10,  # Taille des points
    #                         symbol='circle',  # Type de marqueur (vous pouvez choisir parmi divers symboles)
    #                         line=dict(
    #                             color='white',  # Couleur de la bordure des points
    #                             width=2  # Largeur de la bordure des points
    #                         )
    #                   ))


st.plotly_chart(plot1)







