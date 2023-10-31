from app import db
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from sqlalchemy import func


def count_verified_interests_in_cities(city_names):
    query = (
        db.session.query(Town.name, func.count(PointInterest.name).label("count_pi"))
        .join(Quartier, Quartier.town_id == Town.id)
        .join(PointInterest, PointInterest.quartier_id == Quartier.id)
        .filter(PointInterest.is_verify == 1)
        .filter(Town.name.in_(city_names))
        .group_by(Town.name)
        .order_by(func.count(PointInterest.name).desc())
    )

    result = query.all()
    return result
