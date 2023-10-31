from app import db
from app.models.town import Town
from app.models.quartier import Quartier
from app.models.point_interest import PointInterest
from app.models.category import Category
from sqlalchemy import func


def calculate_distraction_quartier(town_name, category_name):
    query = (
        db.session.query(
            Quartier.name.label("quartier_name"),
            func.count(PointInterest.id).label("distraction_count"),
        )
        .join(PointInterest, Quartier.id == PointInterest.quartier_id, isouter=True)
        .join(Category, PointInterest.category_id == Category.id, isouter=True)
        .join(Town, Quartier.town_id == Town.id)
        .filter(Town.name == town_name)
        .filter(Category.name == category_name)
        .group_by(Quartier.name)
        .order_by(func.count(PointInterest.id).desc())
        .limit(5)
    )

    result = query.all()
    return result
