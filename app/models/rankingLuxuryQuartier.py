from app.database import db
from app.models.price import Price
from app.models.point_interest import PointInterest
from app.models.quartier import Quartier
from app.models.town import Town
from app.models.category import Category
from sqlalchemy import desc, func
from sqlalchemy.exc import SQLAlchemyError

from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy.pool import Pool


def rankingLuxuryQuartier(towns, category_name):
    try:
        query = (
            db.session.query(
                Quartier.name.label("quartier_name"),
                func.avg(Price.amount).label("average_amount"),
                func.avg(PointInterest.etoile).label("average_etoile"),
            )
            .join(Price, Price.pointinteret_id == PointInterest.id)
            .join(Category, Category.id == PointInterest.category_id)
            .join(Quartier, Quartier.id == PointInterest.quartier_id)
            .join(Town, Town.id == Quartier.town_id)
            .filter(Town.name.in_(towns))
            .filter(Category.name == "Hôtel")
            .group_by(PointInterest.name, Quartier.name, Town.name)
            .having(PointInterest.etoile > 3)
            .order_by(desc("average_price"))
            .limit(5)
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
