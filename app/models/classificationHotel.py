from app.database import db
from app.models.price import Price
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.category import Category
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy.pool import Pool


def classificationHotel(town_name, language, category_name):
    try:
        query = (
            db.session.query(
                PointInterest.name, PointInterest.etoile, Quartier.name, Town.name
            )
            .select_from(Town)
            .join(Quartier, Town.id == Quartier.town_id)
            .join(PointInterest, Quartier.id == PointInterest.quartier_id)
            .join(Category, PointInterest.category_id == Category.id)
            .filter(Town.name == town_name)
            .filter(Category.name == category_name)
            .filter(PointInterest.etoile > 3)
            .group_by(PointInterest.name)
        )

        result = query.all()

        db.session.commit()

        return result
    except SQLAlchemyError as e:
        # Gérez l'exception ici, par exemple, en journalisant l'erreur.
        # Vous pouvez également effectuer des actions de nettoyage ou de notification si nécessaire.
        print(f"Une erreur SQLAlchemy s'est produite : {e}")
        db.session.rollback()
        return None  # Ou une autre valeur par défaut ou comportement de secours
    finally:
        db.session.close()  # Assurez-vous de fermer la session SQLAlchemy, même en cas d'exception.
