# app/models/averageInterest.py

from app import db
from app.models.price import Price
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.category import Category
from sqlalchemy import func


def calculate_average_interest(town_name, language, category_name):
    query = (
        db.session.query(
            Town.name, func.count(PointInterest.id), func.avg(Price.amount)
        )
        .join(Quartier, Quartier.town_id == Town.id)
        .join(PointInterest, PointInterest.quartier_id == Quartier.id)
        .join(Price, Price.pointinteret_id == PointInterest.id)
        .join(Category, Category.id == PointInterest.category_id)
        .filter(Town.name == town_name)
        .filter(Price.langue == language)
        .filter(Category.name == category_name)
        .group_by(Town.name)
    )

    result = query.all()
    return result
