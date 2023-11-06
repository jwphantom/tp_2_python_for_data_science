from app.database import db
from app.models.town import Town
from app.models.quartier import Quartier
from app.models.point_interest import PointInterest
from app.models.category import Category
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError


def calculate_distraction_quartier(town_name, category_name):
    try:
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
