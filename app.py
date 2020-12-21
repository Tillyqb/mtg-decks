from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from model import connect_to_db, db
from generate_secret_key import genterate_secret_key

app = Flask(__name__)

SECRET_KEY = genterate_secret_key(256)


@app.route('')
def homepage():
    return render_template("root.html")


if __name__ == "__main__":
    connect_to_db()
    app.run(debug=True, host='0.0.0.0')
