from flask import (
    jsonify,
    request,
)  # Importez request pour accéder aux paramètres de l'URL
from flask import Blueprint
from app.models.averageInterest import calculate_average_interest
import json  # Importez le module json

# Créez une instance Blueprint pour les routes liées à l'average_interest
average_interest_bp = Blueprint("average_interest", __name__)


@average_interest_bp.route(
    "/average_interest/<town_name>/<category_name>", methods=["GET"]
)
def get_average_interest(town_name, category_name):
    result = calculate_average_interest(town_name, "fr", category_name)

    # Convertissez le résultat en une structure JSON-friendly
    json_result = [
        {"town_name": row[0], "average_amount": float(row[1])} for row in result
    ]

    # Utilisez le module json pour convertir response_data en JSON et assurez-vous que ensure_ascii est False
    return json.dumps(json_result, default=str, ensure_ascii=False)
