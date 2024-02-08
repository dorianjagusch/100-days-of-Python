from flask import Flask, render_template
from my_form import MyForm
from flask_bootstrap import Bootstrap5
import dotenv, os

dotenv.load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("CSRF_TOKEN")
bootstrap = Bootstrap5(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():

    my_form = MyForm()
    if my_form.validate_on_submit():
        if my_form.email.data == "admin@email.com" and my_form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=my_form)


if __name__ == '__main__':
    app.run(debug=True)
