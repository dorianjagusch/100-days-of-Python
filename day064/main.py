from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Optional
import dotenv
import os
import requests

dotenv.load_dotenv()

MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_TOKEN = os.getenv("MOVIE_DB_TOKEN")

headers = {"Authorization": "Bearer " + MOVIE_DB_TOKEN}

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CREATE TABLE

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String, unique=True)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=True)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# FORMS

class EditForm(FlaskForm):
    rating = DecimalField("Your rating out of 10 🌟", validators=[Optional(), NumberRange(0, 10)])
    review = StringField("Your review", validators=[Optional()])
    submit = SubmitField("Submit")


class NewMovieForm(FlaskForm):
    title = StringField("Movie title", validators=[Optional()])
    submit = SubmitField("Add Movie")
    cancel = SubmitField("Cancel")


@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i

    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/delete")
def delete():
    movie_id = request.args.get("id")
    to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for("home"))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get("id")
    to_edit = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        if form.rating.data:
            to_edit.rating = form.rating.data
        if form.review.data:
            to_edit.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=to_edit, form=form)


@app.route("/add_movie")
def add_movie():
    movie_id = request.args.get("movie_id")
    response = requests.get(MOVIE_DB_INFO_URL + "/" + movie_id, headers=headers)
    movie_data = response.json()
    new_movie = Movie(title=movie_data["title"],
                      year=movie_data["release_date"].split("-")[0],
                      description=movie_data["overview"],
                      rating=0,
                      ranking=100,
                      review="",
                      img_url=f"{MOVIE_DB_IMAGE_URL}{movie_data['poster_path']}"
                      )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))


@app.route("/add", methods=["GET", "POST"])
def add():
    movie_form = NewMovieForm()
    if movie_form.validate_on_submit():
        if movie_form.cancel.data:
            return redirect(url_for('home'))
        params = {"query": movie_form.title.data}
        try:
            response = requests.get(MOVIE_DB_SEARCH_URL, params=params, headers=headers)
            response.raise_for_status()
        except requests.RequestException:
            return render_template("add.html", form=movie_form)
        search_results = response.json()["results"]
        return render_template("select.html", search_results=search_results)

    return render_template("add.html", form=movie_form)


if __name__ == '__main__':
    app.run(debug=True)
