from flask import render_template
from app import app
from sqlalchemy.exc import OperationalError


# Gestionnaire d'erreur 404 (Page non trouvée)
@app.errorhandler(404)
def not_found_error(error):
    return render_template("errors/404.html"), 404


# Gestionnaire d'erreur 500 (Internal Server Error)
@app.errorhandler(500)
def internal_error(error):
    return render_template("errors/500.html"), 500


@app.errorhandler(OperationalError)
def handle_sqlalchemy_operational_error(error):
    # Log l'erreur ou effectuez d'autres actions de gestion des erreurs
    # Vous pouvez également personnaliser la page d'erreur à afficher
    return render_template("errors/500.html"), 500
