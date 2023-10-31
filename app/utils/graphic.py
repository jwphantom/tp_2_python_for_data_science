import base64
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.figure import Figure
import numpy as np


class GraphicGenerator:
    @staticmethod
    def generate_histogram(data, town_names):
        fig = Figure()
        ax = fig.subplots()

        x_values = range(1, len(data) + 1)

        colors = ["#5B47FB", "#9e93ff", "#8275f9", "orange", "purple"]

        ax.bar(x_values, data, align="center", color=colors)

        ax.set_xticks(x_values)
        ax.set_xticklabels(town_names)

        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        imageBase64 = "data:image/png;base64," + data

        return imageBase64

    @staticmethod
    def generate_pie_chart(data, labels):
        fig = Figure()
        ax = fig.subplots()

        ax.pie(
            data,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90,
            colors=["#5B47FB", "#04AA6D", "#8275f9", "orange", "#9BD5DC"],
        )

        buf = BytesIO()
        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        imageBase64 = "data:image/png;base64," + data

        return imageBase64
