from app.database import db
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError


def count_verified_interests_in_cities(city_names):
    try:
        query = (
            db.session.query(
                Town.name, func.count(PointInterest.name).label("count_pi")
            )
            .join(Quartier, Quartier.town_id == Town.id)
            .join(PointInterest, PointInterest.quartier_id == Quartier.id)
            .filter(PointInterest.is_verify == 1)
            .filter(Town.name.in_(city_names))
            .group_by(Town.name)
            .order_by(func.count(PointInterest.name).desc())
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
