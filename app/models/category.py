# app/models/category.py

from app import db


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    slug = db.Column(db.String(255))
    langue = db.Column(db.String(10))
    icon = db.Column(db.String(255))
    is_translate = db.Column(db.Boolean)
    translate_id = db.Column(db.Integer)
    parent_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    def __init__(
        self,
        name,
        slug,
        langue,
        icon,
        is_translate,
        translate_id,
        parent_id,
        created_at,
        updated_at,
    ):
        self.name = name
        self.slug = slug
        self.langue = langue
        self.icon = icon
        self.is_translate = is_translate
        self.translate_id = translate_id
        self.parent_id = parent_id
        self.created_at = created_at
        self.updated_at = updated_at

    def __repr__(self):
        return f"<Category {self.name}>"
