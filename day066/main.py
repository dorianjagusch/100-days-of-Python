from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random
from dataclasses import dataclass

SECRET_API_KEY = "123456789"

app = Flask(__name__)


# CREATE DB
class Base(DeclarativeBase):
    pass


# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)



# Cafe TABLE Configuration

@dataclass
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record

@app.route("/all", methods=["GET"])
def get_all_cafes():
    cafe_records = db.session.query(Cafe).order_by(Cafe.name)
    return jsonify(cafes=[cafe.to_dict() for cafe in cafe_records])


@app.route("/search", methods=["GET"])
def search_cafes():
    location = request.args.get("loc")
    result_cafes = db.session.execute(db.select(Cafe).where(Cafe.location == location)).scalars().all()
    if result_cafes:
        return jsonify(cafes=[cafe.to_dict() for cafe in result_cafes])
    return jsonify(error={"Not Found": "No cafe at that location known to us"}), 404


@app.route("/random", methods=["GET"])
def get_random_cafe():
    cafe_records = db.session.execute(db.select(Cafe)).scalars()
    rand_cafe = random.choice(cafe_records.all())
    return jsonify(cafe=rand_cafe)


# HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def add_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price")
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Added cafe successfully to the database"}), 201


# HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        print(request.args.get("new_price"))
        price = float(request.args.get("new_price"))
    except TypeError:
        return jsonify({"error": {"Type": "Provide a price as float"}}), 400
    if not price or int(price) < 0:
        return jsonify({"error": {"Input": "Provide a price to change it"}}),  400
    to_patch = db.get_or_404(Cafe, cafe_id)
    to_patch.coffee_price = price
    db.session.commit()
    return jsonify({"success": "Coffee price was successfully changed"}), 200


# HTTP DELETE - Delete Record

@app.route("/delete/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api_key") != SECRET_API_KEY:
        return jsonify({"Error": {"Not authorised": "You are not authorised for this operation"}}), 403
    to_delete = db.get_or_404(Cafe, cafe_id)
    db.session.delete(to_delete)
    db.session.commit()
    return jsonify({"success": "Cafe was successfully deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)
