from flask import Flask, render_template
import requests
from requests import exceptions

app = Flask(__name__)

try:
    response = requests.get("https://api.npoint.io/6973105f53b942a077bf")
    response.raise_for_status()
except exceptions.RequestException:
    posts = []
else:
    posts = response.json()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:post_id>")
def show_post(post_id):
    for post in posts:
        if post_id == post["id"]:
            requested_post = post
            return render_template("post.html", post=post)
    return []


if __name__ == "__main__":
    app.run(debug=True)