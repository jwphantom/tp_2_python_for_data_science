import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.classificationHotel import classificationHotel
import math
import matplotlib.pyplot as plt

from app.utils.graphic import GraphicGenerator


average_interest_bp = Blueprint("average_interest", __name__)


# route qui gère la classification des hôtels supérieur à 3 étoiles
@app.route("/classification", methods=["GET"])
def classification():
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]
    category_name = "Hôtel"
    language = "fr"

    # Liste des catégories
    category_names = "hôtel"

    hotel_result = {}

    for town_name in town_names:
        data = classificationHotel(town_name, language, category_name)
        town_data = []
        for d in data:
            result = {
                "hotel": d[0],
                "etoile": d[1],
                "quartier": d[2],
                "town": town_name,
            }
            town_data.append(result)
        hotel_result[town_name] = town_data

    print(hotel_result)

    return render_template(
        "classification.html",
        page="classification",
        hotel_result=hotel_result,
    )
