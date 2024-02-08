from flask import Flask, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from dataclasses import dataclass

'''
Make sure the required packages are installed: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap5(app)


# CREATE DATABASE
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


with app.app_context():
    db.create_all()


# Forms
class NewPostForm(FlaskForm):
    title = StringField("Post title:", validators=[DataRequired()])
    subtitle = StringField("Subtitle:", validators=[DataRequired()])
    author = StringField("Author:", validators=[DataRequired()])
    img_url = URLField("Image URL:", validators=[DataRequired(), URL()])
    body = CKEditorField("Content:", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    posts = db.session.query(BlogPost).all()
    return render_template("index.html", all_posts=posts)


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    requested_post = db.get_or_404(BlogPost, post_id)
    return render_template("post.html", post=requested_post)


@app.route('/add_post', methods=["GET", "POST"])
def add_post():
    new_post_form = NewPostForm()
    if new_post_form.validate_on_submit():
        new_post = BlogPost(
            title=new_post_form.title.data,
            subtitle=new_post_form.subtitle.data,
            author=new_post_form.author.data,
            img_url=new_post_form.img_url.data,
            body=new_post_form.body.data,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template("make-post.html", form=new_post_form)


# TODO: edit_post() to change an existing blog post

@app.route('/edit_post/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    to_edit = db.get_or_404(BlogPost, post_id)
    edit_post_form = NewPostForm(
        title=to_edit.title,
        subtitle=to_edit.subtitle,
        author=to_edit.author,
        img_url=to_edit.img_url,
        body=to_edit.body,
        date=to_edit.date
    )
    if edit_post_form.validate_on_submit():
        to_edit.title = edit_post_form.title.data
        to_edit.subtitle = edit_post_form.subtitle.data
        to_edit.author = edit_post_form.author.data
        to_edit.img_url = edit_post_form.img_url.data
        to_edit.body = edit_post_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post_id))
    return render_template("make-post.html", form=edit_post_form)


@app.route("/delete/<int:post_id>", methods=["GET"])
def delete_post(post_id):
    to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(to_delete)
    db.session.commit()
    return redirect(url_for("get_all_posts"))


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
