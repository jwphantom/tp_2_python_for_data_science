# Importations de bibliothèques et de modules
import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.averageInterest import calculate_average_interest
import math
import matplotlib.pyplot as plt

# Crée un Blueprint pour les routes liées à l'intérêt moyen
average_interest_bp = Blueprint("average_interest", __name__)

from flask import Flask, redirect


# Définition d'une route Flask pour la page d'accueil ("/") en utilisant la méthode GET
@app.route("/", methods=["GET"])
def index():
    # Redirige l'utilisateur vers la route "/average" avec le code de réponse 302 (redirection temporaire)
    return redirect("/average", code=302)
