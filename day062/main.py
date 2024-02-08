from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
import csv

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


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = URLField('Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    opening_time = TimeField("Opening Time", validators=[DataRequired()])
    closing_time = TimeField("Closing Time", validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating",
                                choices = ["✘"] + ["☕️" * i for i in range(1,6)], coerce=str,
                                validators=[DataRequired()])
    power_rating = SelectField("Power Rating",
                               choices= ["✘"] +["💪" * i for i in range(1,6)], coerce=str,
                               validators=[DataRequired()])
    wifi_rating = SelectField("Wi-Fi Rating",
                              choices= ["✘"] + ["🔌" * i for i in range(1,6)], coerce=str,
                              validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print(form.coffee_rating.data)
        with open("cafe-data.csv", "a") as file:
            new_row = ",".join([
                form.cafe.data,
                form.location.data,
                form.opening_time.data.strftime("%H:%M %p"),
                form.closing_time.data.strftime("%H:%M %p"),
                form.coffee_rating.data,
                form.power_rating.data,
                form.wifi_rating.data
            ])
            file.write("\n" + new_row)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        all_rows = []
        for row in csv_data:
            all_rows.append(row)
    return render_template('cafes.html', cafes=all_rows)


if __name__ == '__main__':
    app.run(debug=True)
