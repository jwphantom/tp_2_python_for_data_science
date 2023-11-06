# Importations de bibliothèques et de modules
import json
from flask import Blueprint, render_template
from app import app
from app.database import db
from app.models.category import Category
from app.models.classificationHotel import classificationHotel
from app.models.rankingLuxuryQuartier import rankingLuxuryQuartier
import math
import matplotlib.pyplot as plt
from app.models.luxuryQuartier import calculate_luxury_hotel

# Crée un Blueprint pour les routes liées au classement des quartiers les plus luxueux
average_interest_bp = Blueprint("average_interest", __name__)


# Définition d'une route Flask pour "/luxury" en utilisant la méthode GET
@app.route("/luxury", methods=["GET"])
def luxury():
    # Liste des noms de villes
    town_names = ["Yaoundé", "Douala", "Bafoussam"]

    # Nom de la catégorie (Hôtel)
    category_name = "Hôtel"

    # Dictionnaire pour stocker les résultats du classement des quartiers les plus luxueux
    quartier_result = {}

    # Appel initial pour le calcul des hôtels de luxe (avec des arguments vides)
    calculate_luxury_hotel("", "")

    # Boucle pour effectuer le calcul des hôtels de luxe pour chaque ville
    for town_name in town_names:
        data = calculate_luxury_hotel(town_name, category_name)
        town_data = []
        if data is not None:  # Vérifie si les données ne sont pas nulles
            for d in data:
                result = {
                    "name": d[0],
                    "avg_amount": math.ceil(d[1]),
                    "avg_star": math.ceil(d[2]),
                    "town": town_name,
                }
                town_data.append(result)
        quartier_result[town_name] = town_data

    # Renvoie un modèle HTML avec des données pour l'affichage
    return render_template(
        "luxury.html",
        page="luxury",
        quartier_result=quartier_result,
    )
