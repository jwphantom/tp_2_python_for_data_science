# Importations de bibliothèques et de modules
import json
from flask import Blueprint, render_template
from app import app
from app.models.category import Category
from app.models.countHotelEtoile import countHotelEtoile
from app.models.classificationHotel import classificationHotel
import math
import matplotlib.pyplot as plt
from app.utils.graphic import GraphicGenerator

# Crée un Blueprint pour les routes liées à la classification des hôtels
average_interest_bp = Blueprint("average_interest", __name__)


# Définition d'une route Flask pour "/classification" en utilisant la méthode GET
@app.route("/classification", methods=["GET"])
def classification():
    # Liste des noms de villes
    town_names = ["Douala", "Yaoundé", "Garoua", "Bafoussam"]

    # Nom de la catégorie (Hôtel)
    category_name = "Hôtel"

    # Langue par défaut (français)
    language = "fr"

    # Dictionnaire pour stocker les résultats de la classification des hôtels
    hotel_result = {}

    # Dictionnaire pour stocker les résultats du décompte des étoiles
    count_result = {}

    # Appel initial pour la classification des hôtels (avec des arguments vides)
    data = classificationHotel("", "", "")

    # Boucle pour effectuer le décompte des étoiles deux fois
    for i in range(2):
        count_result = countHotelEtoile(town_names, language, category_name)

    # Génère un graphique en secteurs pour le décompte des étoiles
    countEtoile_dataGraph = GraphicGenerator.generate_pie_chart(
        [entry[1] for entry in count_result], [item[0] for item in count_result]
    )

    # Boucle sur les noms de villes pour effectuer la classification des hôtels
    for town_name in town_names:
        data = classificationHotel(town_name, language, category_name)
        town_data = []
        if data is not None:
            for d in data:
                result = {
                    "hotel": d[0],
                    "etoile": d[1],
                    "quartier": d[2],
                    "town": town_name,
                }
                town_data.append(result)

        # Ajoute les résultats au dictionnaire des résultats des hôtels par ville
        hotel_result[town_name] = town_data

    # Renvoie un modèle HTML avec des données pour l'affichage
    return render_template(
        "classification.html",
        page="classification",
        hotel_result=hotel_result,
        countEtoile_dataGraph=countEtoile_dataGraph,
    )
