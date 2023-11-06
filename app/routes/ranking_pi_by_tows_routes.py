import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.recommandePI import count_verified_interests_in_cities
import math
import matplotlib.pyplot as plt

from app.utils.graphic import GraphicGenerator


average_interest_bp = Blueprint("average_interest", __name__)


@app.route("/rankingPI", methods=["GET"])
def rankingPI():
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]

    # requête vide en cas d'echec pour relancer la connexion
    count_verified_interests_in_cities("")

    # Résultats pour la catégorie "hôtel"
    rankingPI = []

    for i in range(2):
        rankingPI = count_verified_interests_in_cities(town_names)

        print(rankingPI)

    rankingPI_dataGraph = GraphicGenerator.generate_histogram(
        [entry[1] for entry in rankingPI], [item[0] for item in rankingPI]
    )

    print(rankingPI_dataGraph)

    return render_template(
        "rankingPI.html",
        page="rankingPI",
        rankingPI=rankingPI,
        rankingPI_dataGraph=rankingPI_dataGraph,
    )
