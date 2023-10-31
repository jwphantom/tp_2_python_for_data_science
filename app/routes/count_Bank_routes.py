import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.countBank import calculate_bank_count_by_town
import math
import matplotlib.pyplot as plt

from app.utils.graphic import GraphicGenerator


average_interest_bp = Blueprint("average_interest", __name__)


@app.route("/bank", methods=["GET"])
def bank():
    town_names = ["Yaoundé", "Douala", "Garoua", "Bafoussam"]

    category_name = "DAB & Banques"

    # Résultats pour la catégorie "hôtel"
    countBank = []

    countBank = calculate_bank_count_by_town(town_names, category_name)

    print(countBank)

    countBank_dataGraph = GraphicGenerator.generate_histogram(
        [entry[1] for entry in countBank], [item[0] for item in countBank]
    )

    return render_template(
        "countBank.html",
        page="bank",
        countBank=countBank,
        countBank_dataGraph=countBank_dataGraph,
    )
