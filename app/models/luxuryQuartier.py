from app.database import db
from app.models.point_interest import PointInterest
from app.models.category import Category
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.price import Price
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError


def calculate_luxury_hotel(town_name, category_name):
    try:
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
            .order_by(
                func.avg(Price.amount).desc(), func.avg(PointInterest.etoile).desc()
            )
            .limit(5)
        )
        db.session.commit()

        result = query.all()
        return result
    except SQLAlchemyError as e:
        # Gérez l'exception ici, par exemple, en journalisant l'erreur.
        # Vous pouvez également effectuer des actions de nettoyage ou de notification si nécessaire.
        print(f"Une erreur SQLAlchemy s'est produite : {e}")
        db.session.rollback()

        return None  # Ou une autre valeur par défaut ou comportement de secours
    finally:
        db.session.close()  # Assurez-vous de fermer la session SQLAlchemy, même en cas d'exception.
