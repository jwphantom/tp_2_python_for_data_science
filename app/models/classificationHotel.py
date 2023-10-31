# app/models/averageInterest.py

from app import db
from app.models.price import Price
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.category import Category
from sqlalchemy import func


def classificationHotel(town_name, language, category_name):
    query = (
        db.session.query(
            PointInterest.name, PointInterest.etoile, Quartier.name, Town.name
        )
        .join(Category, Category.id == PointInterest.category_id)
        .join(Quartier, Quartier.id == PointInterest.quartier_id)
        .join(Town, Town.id == Quartier.town_id)
        .filter(Town.name == town_name)
        .filter(Category.name == category_name)
        .filter(PointInterest.langue == language)
        .group_by(PointInterest.name)
        .having(PointInterest.etoile > 3)
    )

    result = query.all()
    return result
