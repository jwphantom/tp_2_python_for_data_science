import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.averageInterest import calculate_average_interest
import math
import matplotlib.pyplot as plt

from app.utils.graphic import GraphicGenerator


average_interest_bp = Blueprint("average_interest", __name__)


@app.route("/average", methods=["GET"])
def average():
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]
    category_name = "restaurant"
    language = "fr"

    # Liste des catégories
    category_names = ["restaurant", "hôtel"]

    # Résultats pour la catégorie "restaurant"
    restaurant_result = []

    # Résultats pour la catégorie "hôtel"
    hotel_result = []

    # requête vide en cas d'echec pour relancer la connexion

    for town_name in town_names:
        calculate_average_interest("", "", "")

        for category_name in category_names:
            data = calculate_average_interest(town_name, language, category_name)
            if data:
                result = {
                    "town_name": town_name,
                    "category_name": category_name,
                    "count_point": data[0][1],
                    "average_amount": math.ceil(data[0][2]),
                }
            else:
                result = {
                    "town_name": town_name,
                    "category_name": 0,
                    "count_point": 0,
                    "average_amount": 0,
                }

            if category_name == "restaurant":
                restaurant_result.append(result)
            elif category_name == "hôtel":
                hotel_result.append(result)

    print(hotel_result)

    restaurant_data = GraphicGenerator.generate_histogram(
        [entry["average_amount"] for entry in hotel_result], town_names
    )

    return render_template(
        "average.html",
        page="average",
        town_data=restaurant_result,
        restaurant_data=restaurant_data,
    )
