import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("training_dataset.csv")

st.set_page_config(page_title="Oliist Dataset")
st.header("Study of shipping VS Orders revenues - Olist Dataset")
st.markdown("shipping revenues detailes.")
st.sidebar.header("Variable Comparison")

options = st.sidebar.radio("Select comparison",
                           options=["Shipping Revenues Detailes",
                                    "payments Rvenues Detailes"])

if options == "Shipping Revenues Detailes":

    colors = [(1/256,217/256,132/256), (249/256,185/256,0/256), (241/256,62/256,92/256),\
                    (31/256,69/256,232/256)] #Vert, Jaune, Rouge, Bleu

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, squeeze=False, figsize=(20, 10))
    sns.boxplot(data=df['freight_value'], showfliers=False, ax=ax1, color = colors[0])
    sns.boxplot(data=df['freight_value'], showfliers=True, ax=ax2, color = colors[1])
    sns.histplot(data=df['freight_value'], ax=ax3, color = colors[2])
                        # sum_price ="calculated price by: " +str(olist_orderitems_product.groupby("product_category_name")["price"].sum())
                        # print(sum_price)
    frieght_value_total = 'Total shipping revenues:' +str(df['freight_value'].sum())
                        # print(frieght_value_total)
    ax4.text(0.2, 1.0, frieght_value_total, fontsize=20, ha='left', va='center')
                        # ax4.text(0.2, 0.8, somme_payment_outlier, fontsize=20, ha='left', va='center')
    ax4.axis('off')
    ax1.set_title('freight without std')
    ax2.set_title('freight with std')
    ax3.set_title('freight hist')
                        #  st.pyplot(fig)
                    
elif options == "payments Rvenues Detailes":
    colors = [(1/256,217/256,132/256), (249/256,185/256,0/256), (241/256,62/256,92/256),\
                    (31/256,69/256,232/256)] #Vert, Jaune, Rouge, Bleu

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, squeeze=False, figsize=(20, 10))
    sns.boxplot(data=df['price'], showfliers=False, ax=ax1, color = colors[0])
    sns.boxplot(data=df['price'], showfliers=True, ax=ax2, color = colors[1])
    sns.histplot(data=df['price'], ax=ax3, color = colors[2])
                        # sum_price ="calculated price by: " +str(olist_orderitems_product.groupby("product_category_name")["price"].sum())
                        # print(sum_price)
    frieght_value_total = 'Total Payment:' +str(df['price'].sum())
                        # print(frieght_value_total)
    ax4.text(0.2, 1.0, frieght_value_total, fontsize=20, ha='left', va='center')
                        # ax4.text(0.2, 0.8, somme_payment_outlier, fontsize=20, ha='left', va='center')
    ax4.axis('off')
    ax1.set_title('payments without std')
    ax2.set_title('payments with std')
    ax3.set_title('payments hist')                       
st.pyplot(fig)

