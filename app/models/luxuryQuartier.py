from app import db
from app.models.point_interest import PointInterest
from app.models.category import Category
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.price import Price
from sqlalchemy import func


def calculate_luxury_hotel(town_name, category_name):
    query = (
        db.session.query(
            Quartier.name.label("quartier_name"),
            func.avg(Price.amount).label("average_amount"),
            func.avg(PointInterest.etoile).label("average_etoile"),
        )
        .join(Town, Town.id == Quartier.town_id)
        .join(PointInterest, PointInterest.quartier_id == Quartier.id)
        .join(Price, Price.pointinteret_id == PointInterest.id)
        .join(Category, Category.id == PointInterest.category_id)
        .filter(Town.name == town_name)
        .filter(Category.name == category_name)
        .group_by(Quartier.name)
        .order_by(func.avg(Price.amount).desc(), func.avg(PointInterest.etoile).desc())
        .limit(5)
    )

    result = query.all()
    return result
