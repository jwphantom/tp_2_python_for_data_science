# Importations de bibliothèques et de modules
import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.recommandePI import count_verified_interests_in_cities
import math
import matplotlib.pyplot as plt

from app.utils.graphic import GraphicGenerator

# Crée un Blueprint pour les routes liées au classement PI (Points d'Intérêt)
average_interest_bp = Blueprint("average_interest", __name__)


# Définition d'une route Flask pour "/rankingPI" en utilisant la méthode GET
@app.route("/rankingPI", methods=["GET"])
def rankingPI():
    # Liste des noms de villes
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]

    # Appel initial pour le décompte des intérêts vérifiés dans les villes (avec des arguments vides)
    count_verified_interests_in_cities("")

    # Liste pour stocker les résultats du classement PI
    rankingPI = []

    # Boucle pour effectuer le décompte des intérêts vérifiés dans les villes deux fois
    for i in range(2):
        rankingPI = count_verified_interests_in_cities(town_names)

    # Génère un histogramme pour le classement PI
    rankingPI_dataGraph = GraphicGenerator.generate_histogram(
        [entry[1] for entry in rankingPI], [item[0] for item in rankingPI]
    )

    # Renvoie un modèle HTML avec des données pour l'affichage
    return render_template(
        "rankingPI.html",
        page="rankingPI",
        rankingPI=rankingPI,
        rankingPI_dataGraph=rankingPI_dataGraph,
    )
