import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.coinsChaud import calculate_distraction_quartier
import math
import matplotlib.pyplot as plt

from app.utils.graphic import GraphicGenerator


average_interest_bp = Blueprint("average_interest", __name__)


@app.route("/coins-chauds", methods=["GET"])
def coinsChauds():
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]
    category_name = "Coins chauds"
    language = "fr"

    # Résultats pour la catégorie "coins chauds"
    coins_Chauds = {}

    for town_name in town_names:
        data = calculate_distraction_quartier(town_name, category_name)
        quartier_data = []
        for d in data:
            if d:
                result = {
                    "quartier": d[0],
                    "count": d[1],
                }
            else:
                result = {
                    "quartier": "",
                    "count": 0,
                }
            quartier_data.append(result)
        coins_Chauds[town_name] = quartier_data

    coins_Chauds_data = []
    label_data = []

    for city, quartiers in coins_Chauds.items():
        quartier_counts = [quartier["count"] for quartier in quartiers]
        coins_Chauds_data.append(quartier_counts)

        label = [quartier["quartier"] for quartier in quartiers]
        label_data.append(label)

    imagesBase64 = []
    index = 0
    for item in coins_Chauds_data:
        print(item)
        image = GraphicGenerator.generate_pie_chart(item, label_data[index])
        imagesBase64.append(image)
        index += 1

    print(len(imagesBase64))

    return render_template(
        "coinsChauds.html",
        page="coins-chauds",
        coins_Chauds=coins_Chauds,
        imagesBase64=imagesBase64,
    )
