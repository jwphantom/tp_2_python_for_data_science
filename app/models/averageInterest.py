from app.database import db
from app.models.price import Price
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.category import Category
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError
from flask import g, redirect, url_for


def calculate_average_interest(town_name, language, category_name):
    try:
        query = (
            db.session.query(
                Town.name, func.count(PointInterest.id), func.avg(Price.amount)
            )
            .join(Quartier, Quartier.town_id == Town.id)
            .join(PointInterest, PointInterest.quartier_id == Quartier.id)
            .join(Price, Price.pointinteret_id == PointInterest.id)
            .join(Category, Category.id == PointInterest.category_id)
            .filter(Town.name == town_name)
            .filter(Price.langue == language)
            .filter(Category.name == category_name)
            .group_by(Town.name)
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
