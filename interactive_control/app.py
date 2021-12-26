from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
from sqlalchemy.orm import sessionmaker


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///spalvos.db"
app.config["SQLALCHEMY_BINDS"] = {"spalvos_mikroschemai": "sqlite:///spalvos_mikroschemai.db"}
db = SQLAlchemy(app)

# Pirma duomenu baze su spalvomis
class Spalvynas(db.Model):
    __tablename__ = "Spalvynas"
    id = db.Column(db.Integer, primary_key=True)
    spalva = db.Column("Spalva", db.String)
    r = db.Column("R", db.Integer)
    g = db.Column("G", db.Integer)
    b = db.Column("B", db.Integer)

    def __init__(self, spalva, r, g, b):
        self.spalva = spalva
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f"{self.id}. {self.spalva}: ({self.r}, {self.g}, {self.b})"

# Antra duomenu baze su pasirinkta spalva
class Spalvos_mikroschemai(db.Model):
    __bind_key__ = "spalvos_mikroschemai"
    __tablename__ = "Spalvos mikroschemai"
    id = db.Column(db.Integer, primary_key=True)
    r = db.Column("R", db.Integer)
    g = db.Column("G", db.Integer)
    b = db.Column("B", db.Integer)

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f"({self.r}, {self.g}, {self.b})"


@app.route("/")
def home():
    return render_template("web.html")


@app.route("/spalva", methods=["POST", "GET"])
def spalva():
    if request.method == "POST":
        # gaunama spalvos reiksme:
        pasirinkta_spalva = request.form["spalva"] 
        grazintas_rgb = Spalvynas.query.filter_by(spalva=pasirinkta_spalva).one()
        print(grazintas_rgb)
        r = grazintas_rgb.r
        g = grazintas_rgb.g
        b = grazintas_rgb.b
        print(r, g, b)
        # is antros duomenu bazes istrinami ir pridedami nauji duomenys:
        seni_rgb = Spalvos_mikroschemai.query.all()
        for eilute in seni_rgb:
            db.session.delete(eilute)
        ikelimas = Spalvos_mikroschemai(r, g, b)  # nurodymas gautus duomenis kelti i antra DB
        db.session.add(ikelimas)
        db.session.commit()
        return redirect(url_for("home"))
    elif request.method == "GET":
        # issiunciami duomenys mikroschemai uzklausus:
        siunciama_spalva = Spalvos_mikroschemai.query.one()
        return {"r" : siunciama_spalva.r, "g" : siunciama_spalva.g, "b" : siunciama_spalva.b }


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host="0.0.0.0")        # Naudojamas host=0.0.0.0 norint, kad servisas butu prieinamas is isores. Gautas pasikeites IP adresas.


