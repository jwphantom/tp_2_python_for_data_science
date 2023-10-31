import json
from flask import Blueprint, render_template
from app import app, db
from app.models.category import Category
from app.models.averageInterest import calculate_average_interest
import math
import matplotlib.pyplot as plt


from flask import Flask, redirect


average_interest_bp = Blueprint("average_interest", __name__)


@app.route("/", methods=["GET"])
def index():
    return redirect("/average", code=302)
