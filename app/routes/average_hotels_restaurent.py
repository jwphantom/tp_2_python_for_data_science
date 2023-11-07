# Importations de bibliothèques et de modules
import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.averageInterest import calculate_average_interest
import math
import matplotlib.pyplot as plt
from app.utils.graphic import GraphicGenerator

# Crée un Blueprint pour les routes liées à l'intérêt moyen
average_interest_bp = Blueprint("average_interest", __name__)


# Définition d'une route Flask pour "/average" en utilisant la méthode GET
@app.route("/average", methods=["GET"])
def average():
    # Liste des noms de villes
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]

    # Catégorie par défaut
    category_name = "restaurant"

    # Langue par défaut
    language = "fr"

    # Liste des catégories à analyser
    category_names = ["restaurant", "hôtel"]

    # Liste pour stocker les résultats de la catégorie "restaurant"
    restaurant_result = []

    # Liste pour stocker les résultats de la catégorie "hôtel"
    hotel_result = []

    # Boucle sur les noms de villes
    for town_name in town_names:
        # Appel d'une fonction pour effectuer le calcul de l'intérêt moyen
        calculate_average_interest("", "", "")

        # Boucle sur les catégories
        for category_name in category_names:
            # Appel de la fonction de calcul de l'intérêt moyen
            data = calculate_average_interest(town_name, language, category_name)

            if data:
                # Si des données sont disponibles, crée un dictionnaire de résultats
                result = {
                    "town_name": town_name,
                    "category_name": category_name,
                    "count_point": data[0][1],
                    "average_amount": math.ceil(data[0][2]),
                }
            else:
                # En cas de données manquantes, utilise des valeurs par défaut
                result = {
                    "town_name": town_name,
                    "category_name": 0,
                    "count_point": 0,
                    "average_amount": 0,
                }

            # Ajoute les résultats à la liste appropriée en fonction de la catégorie
            if category_name == "restaurant":
                restaurant_result.append(result)
            elif category_name == "hôtel":
                hotel_result.append(result)

    # Génère des données pour un histogramme des résultats de la catégorie "hôtel"
    restaurant_data = GraphicGenerator.generate_histogram(
        [entry["average_amount"] for entry in hotel_result], town_names
    )

    # Renvoie un modèle HTML avec des données pour l'affichage
    return render_template(
        "average.html",
        page="average",
        town_data=restaurant_result,
        restaurant_data=restaurant_data,
    )
