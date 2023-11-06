import json
from flask import Blueprint, render_template
from app import app
from app.database import db

from app.models.category import Category
from app.models.classificationHotel import classificationHotel
import math
import matplotlib.pyplot as plt

from app.models.luxuryQuartier import calculate_luxury_hotel

average_interest_bp = Blueprint("average_interest", __name__)


# route qui gère le classement des quartiers les plus luxieux
@app.route("/luxury", methods=["GET"])
def luxury():
    town_names = ["Yaoundé", "Douala", "Bafoussam"]
    category_name = "Hôtel"

    # Liste des catégories

    quartier_result = {}

    # requête vide en cas d'echec pour relancer la connexion
    calculate_luxury_hotel("", "")

    for town_name in town_names:
        data = calculate_luxury_hotel(town_name, category_name)
        town_data = []
        if data is not None:  # Check if data is not None
            for d in data:
                result = {
                    "name": d[0],
                    "avg_amount": math.ceil(d[1]),
                    "avg_star": math.ceil(d[2]),
                    "town": town_name,
                }
                town_data.append(result)
        quartier_result[town_name] = town_data

    print(quartier_result)

    return render_template(
        "luxury.html",
        page="luxury",
        quartier_result=quartier_result,
    )
