from app import db
from app.models.town import Town
from app.models.quartier import Quartier
from app.models.point_interest import PointInterest
from app.models.category import Category
from sqlalchemy import func


def calculate_bank_count_by_town(towns, category_name):
    query = (
        db.session.query(
            Town.name.label("town_name"),
            func.count(PointInterest.id).label("bank_count"),
        )
        .join(Quartier, Town.id == Quartier.town_id, isouter=True)
        .join(PointInterest, Quartier.id == PointInterest.quartier_id, isouter=True)
        .join(Category, PointInterest.category_id == Category.id, isouter=True)
        .filter(Town.name.in_(towns))
        .filter(Category.name == category_name)
        .group_by(Town.name)
        .order_by(func.count(PointInterest.id).desc())
    )

    result = query.all()
    return result
