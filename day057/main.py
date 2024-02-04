from flask import Flask, render_template
import requests
from post import Post


response = requests.get(" https://api.npoint.io/c790b4d5cab58020d391")
response.raise_for_status()
all_posts = [Post(**post) for post in response.json()]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    for post in all_posts:
        if post.id == post_id:
            return render_template("post.html", post=post)
    return []


if __name__ == "__main__":
    app.run(debug=True)
