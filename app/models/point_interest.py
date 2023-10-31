# app/models/point_interest.py

from app import db


class PointInterest(db.Model):
    __tablename__ = "point_interests"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    etoile = db.Column(db.Integer)
    address = db.Column(db.String(255))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    description = db.Column(db.String(255))
    status = db.Column(db.String(255))
    is_booking = db.Column(db.Boolean)
    is_verify = db.Column(db.Boolean)
    is_restaurant = db.Column(db.Boolean)
    is_transport = db.Column(db.Boolean)
    is_stadium = db.Column(db.Boolean)
    is_recommand = db.Column(db.Boolean)
    langue = db.Column(db.String(10))
    is_translate = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)
    translate_id = db.Column(db.Integer)
    category_id = db.Column(db.Integer)
    quartier_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(
        self,
        name,
        etoile,
        address,
        longitude,
        latitude,
        description,
        status,
        is_booking,
        is_verify,
        is_restaurant,
        is_transport,
        is_stadium,
        is_recommand,
        langue,
        is_translate,
        user_id,
        translate_id,
        category_id,
        quartier_id,
        created_at,
        updated_at,
    ):
        self.name = name
        self.etoile = etoile
        self.address = address
        self.longitude = longitude
        self.latitude = latitude
        self.description = description
        self.status = status
        self.is_booking = is_booking
        self.is_verify = is_verify
        self.is_restaurant = is_restaurant
        self.is_transport = is_transport
        self.is_stadium = is_stadium
        self.is_recommand = is_recommand
        self.langue = langue
        self.is_translate = is_translate
        self.user_id = user_id
        self.translate_id = translate_id
        self.category_id = category_id
        self.quartier_id = quartier_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<PointInterest {self.name}>"
