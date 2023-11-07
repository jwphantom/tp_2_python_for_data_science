# Importations de bibliothèques et de modules
import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.countBank import calculate_bank_count_by_town
import math
import matplotlib.pyplot as plt
from app.utils.graphic import GraphicGenerator

# Crée un Blueprint pour les routes liées au décompte des banques
average_interest_bp = Blueprint("average_interest", __name__)


# Définition d'une route Flask pour "/bank" en utilisant la méthode GET
@app.route("/bank", methods=["GET"])
def bank():
    # Liste des noms de villes
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]

    # Nom de la catégorie (DAB & Banques)
    category_name = "DAB & Banques"

    # Liste pour stocker les résultats du décompte des banques
    countBank = []

    # Appel initial pour le décompte des banques (avec des arguments vides)
    calculate_bank_count_by_town("", "")

    # Boucle pour effectuer le décompte des banques deux fois
    for i in range(2):
        countBank = calculate_bank_count_by_town(town_names, category_name)

    # Génère un histogramme pour le décompte des banques
    countBank_dataGraph = GraphicGenerator.generate_histogram(
        [entry[1] for entry in countBank], [item[0] for item in countBank]
    )

    # Renvoie un modèle HTML avec des données pour l'affichage
    return render_template(
        "countBank.html",
        page="bank",
        countBank=countBank,
        countBank_dataGraph=countBank_dataGraph,
    )
