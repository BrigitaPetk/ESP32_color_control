from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///spalvos.db"
app.config["SQLALCHEMY_BINDS"] = {"spalvos_mikroschemai": "sqlite:///spalvos_mikroschemai.db"}
db = SQLAlchemy(app)


class Spalvynas(db.Model):
    __tablename__ = "Spalvynas"
    id = db.Column(db.Integer, primary_key=True)
    spalva = db.Column("Spalva", db.String)
    rgb = db.Column("RGB", db.String)

    def __init__(self, spalva, rgb):
        self.spalva = spalva
        self.rgb = rgb

    def __repr__(self):
        return f"{self.id}. {self.spalva}: {self.rgb}"


class Spalvos_mikroschemai(db.Model):
    __bind_key__ = "spalvos_mikroschemai"
    __tablename__ = "Spalvos mikroschemai"
    id = db.Column(db.Integer, primary_key=True)
    rgb = db.Column("RGB", db.String)

    def __init__(self, rgb):
        self.rgb = rgb

    def __repr__(self):
        return f"{self.rgb}"


@app.route("/")
def home():
    return render_template("box2.html")


@app.route("/spalva", methods=["POST", "GET"])
def spalva():
    if request.method == "POST":
        pasirinkta_spalva = request.form["spalva"]  # gavau reiksme, kuria grazina paspaudus mygtuka
        grazintas_rgb = Spalvynas.query.filter_by(spalva=pasirinkta_spalva).one()
        rgb = grazintas_rgb.rgb
        print(rgb)
        print(grazintas_rgb)
        seni_rgb = Spalvos_mikroschemai.query.all()
        for eilute in seni_rgb:
            db.session.delete(eilute)
        ikelimas = Spalvos_mikroschemai(rgb)  # nurodymas gautus duomenis kelti i antra DB
        db.session.add(ikelimas)
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method == "GET":
        pass


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

