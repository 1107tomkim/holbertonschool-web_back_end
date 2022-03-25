#!/usr/bin/env python3
"""Task 1 setting up basic Flask app"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    """Method Index"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
