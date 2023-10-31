# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


# Importation des routes
from app.routes import category_routes
from app.routes import average_hotels_restaurent
from app.routes import classification_hotel
from app.routes import luxury_quartier
from app.routes.average_interest_route import average_interest_bp
from app.routes import index_routes
from app.routes import count_Bank_routes
from app.routes import count_coins_chauds_routes
from app.routes import ranking_pi_by_tows_routes
from app import errors

# importation des fonctions utilitaire
from app.utils.graphic import GraphicGenerator


app.register_blueprint(average_interest_bp)
