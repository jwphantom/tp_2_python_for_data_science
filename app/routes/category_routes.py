from flask import request, jsonify
from app import app, db
from app.models.category import Category


@app.route("/categories", methods=["GET"])
def get_categories():
    categories = Category.query.all()
    category_list = []
    for category in categories:
        category_list.append({"id": category.id, "name": category.name})
    return jsonify(category_list)
