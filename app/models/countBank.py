from app.database import db
from app.models.town import Town
from app.models.quartier import Quartier
from app.models.point_interest import PointInterest
from app.models.category import Category
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError


def calculate_bank_count_by_town(towns, category_name):
    try:
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
    except SQLAlchemyError as e:
        # Gérez l'exception ici, par exemple, en journalisant l'erreur.
        # Vous pouvez également effectuer des actions de nettoyage ou de notification si nécessaire.
        print(f"Une erreur SQLAlchemy s'est produite : {e}")
        db.session.rollback()

        return None  # Ou une autre valeur par défaut ou comportement de secours
    finally:
        db.session.close()  # Assurez-vous de fermer la session SQLAlchemy, même en cas d'exception.
