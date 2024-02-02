import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, accuracy_score, f1_score

import json
import pickle
import numpy as np


def make_model_save():
    df = pd.read_csv("training_dataset.csv")

    # label_encoder = LabelEncoder()
    # df['order_status_encoded'] = label_encoder.fit_transform(df['order_status'])

    # df.to_csv("encoded_data.csv")

    # order_status = df['order_status'].unique()
    # dict_encoder = {int(label): order for label, order in zip(label_encoder.transform(order_status), order_status)}

    # with open('encoder.json', 'w') as write_file:
    #     json.dump(dict_encoder, write_file, indent=4)

    # Separate Target and Features : x and y datas
    y = df['score']
    X= df[["freight_value","price"]]

    # Separate TrainSet / TestSet
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)
    X_train["price"] = X_train["price"].apply(lambda x: x if x<5000 else 5000)
    X_test["price"] = X_test["price"].apply(lambda x: x if x<5000 else 5000)
    
    X_train["freight_value"] = X_train["freight_value"].apply(lambda x: x if x<500 else 500)
    X_test["freight_value"] = X_test["freight_value"].apply(lambda x: x if x<500 else 500)


    # Train model
    model = RandomForestClassifier(max_depth=2, random_state=0)
    model.fit(X_train,y_train)
    # recall_train = round(recall_score(y_train, model.predict(X_train)),4)
    # acc_train = round(accuracy_score(y_train, model.predict(X_train)),4)
    # f1_train = round(f1_score(y_train, model.predict(X_train)),4)
    
    # recall_test = round(recall_score(y_test, model.predict(X_test)),4)
    # acc_test = round(accuracy_score(y_test, model.predict(X_test)),4)
    f1_test = round(f1_score(y_test, model.predict(X_test)),4)

    with open('main_model.pkl', 'wb') as fichier_modele:
        pickle.dump(model, fichier_modele)





