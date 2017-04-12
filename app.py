import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config.DevelopmentConfig")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Cities

@app.route('/getcities')
def getcities():
    res_cities = {}
    res_cities = Cities.query.all()
    return render_template('index.html', res_cities=res_cities)

if __name__ == '__main__':
    app.run()
