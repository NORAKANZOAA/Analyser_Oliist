import json
import pickle
from sklearn.metrics import recall_score, accuracy_score, f1_score


def make_prediction(x):
 with open('main_model.pkl', 'rb') as fichier_modele:
     loaded_model = pickle.load(fichier_modele)
      
    # Charger le modèle à partir du fichier Pickle
    
        
    # Faire la prédiction
 predictions_out = loaded_model.predict(x)

    # print('prediction:', predictions_out)

    # Charger le fichier encoder pour traduire la prédic tion
    # with open('encoder.json') as json_file:
    #     data = json.load(json_file)

    # Conversion prédiction brute --> traduite
    # predictions_string = data[str(int(predictions_out))]

    # Retourne la valeur
 return predictions_out


