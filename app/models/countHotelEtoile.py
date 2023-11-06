from app.database import db
from app.models.price import Price
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.category import Category
from sqlalchemy import distinct, func
from sqlalchemy.exc import SQLAlchemyError


def countHotelEtoile(towns, language, category_name):
    try:
        query = (
            db.session.query(
                Town.name.label("town_name"),
                func.count(distinct(PointInterest.name)).label("hotel_count"),
            )
            .select_from(Town)
            .outerjoin(Quartier, Town.id == Quartier.town_id)
            .outerjoin(PointInterest, Quartier.id == PointInterest.quartier_id)
            .outerjoin(Category, PointInterest.category_id == Category.id)
            .filter(Town.name.in_(towns))
            .filter(Category.name == "Hôtel")
            .filter(PointInterest.etoile > 3)
            .group_by(Town.name)
            .order_by(func.count(PointInterest.id).desc())
        )

        result = query.all()

        db.session.commit()

        return result
    except SQLAlchemyError as e:
        print(f"Une erreur SQLAlchemy s'est produite : {e}")
        db.session.rollback()
        return None
    finally:
        db.session.close()
