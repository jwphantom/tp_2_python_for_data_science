# app/models/price.py

from app import db


class Price(db.Model):
    __tablename__ = "prices"
    id = db.Column(db.Integer, primary_key=True)
    price_name = db.Column(db.String(255))
    amount = db.Column(
        db.Float
    )  # Assurez-vous que le type est approprié pour les montants
    langue = db.Column(db.String(10))
    is_translate = db.Column(db.Boolean)
    translate_id = db.Column(db.Integer)
    pointinteret_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(
        self,
        price_name,
        amount,
        langue,
        is_translate,
        translate_id,
        pointinteret_id,
        created_at,
        updated_at,
    ):
        self.price_name = price_name
        self.amount = amount
        self.langue = langue
        self.is_translate = is_translate
        self.translate_id = translate_id
        self.pointinteret_id = pointinteret_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Price {self.price_name}>"
