# app/models/town.py

from app import db


class Town(db.Model):
    __tablename__ = "towns"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(
        db.String(255)
    )  # Vous pouvez ajuster la longueur en fonction de vos besoins
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    langue = db.Column(db.String(10))
    is_translate = db.Column(db.Boolean)
    country_id = db.Column(db.Integer)
    translate_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(
        self,
        name,
        description,
        longitude,
        latitude,
        langue,
        is_translate,
        country_id,
        translate_id,
        created_at,
        updated_at,
    ):
        self.name = name
        self.description = description
        self.longitude = longitude
        self.latitude = latitude
        self.langue = langue
        self.is_translate = is_translate
        self.country_id = country_id
        self.translate_id = translate_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Town {self.name}>"
