from flask import Flask
import random

app = Flask(__name__)

number = random.randint(1, 10)

SAD_PUPPIES = [
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdtMHExcjFxbGpmMXo2dXF5NWo5aHZ1bXVwY2huNmNiNDc0YW1waiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/12G1D7rPEV5Cfu/giphy.gif",
    "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWdtMHExcjFxbGpmMXo2dXF5NWo5aHZ1bXVwY2huNmNiNDc0YW1waiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/fqst7AVqF6AVLlYklE/giphy.gif",
    "https://media.giphy.com/media/11nQ2iZnQpPkgo/giphy.gif?cid=790b7611agm0q1r1qljf1z6uqy5j9hvumupchn6cb474ampj&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/ySM2PakMSmw7u/giphy.gif?cid=ecf05e47afxum0fp3tugrhwgxnd9yhp6pjheo9lolkarmmx3&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/14dv1oGhoLfa0w/giphy.gif?cid=ecf05e479gy4jf3a8qeevou3qfm8ik7skhto7e09vfgrwy0k&ep=v1_gifs_search&rid=giphy.gif&ct=g",
    "https://media.giphy.com/media/mcHOSTJMjCrjW/giphy.gif?cid=790b7611sa60mq4b16ytndg4frzvek7v0nyr7vaj58xzp7ra&ep=v1_gifs_search&rid=giphy.gif&ct=g",
]

COLOURS = ["red", "orange", "yellow", "blue", "purple"]

@app.route("/")
def start_page():
    return "<h1>Guess a number between 0 and 9</h1>" \
           f"<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3Y0eW9keWs2Mmc3dGwwdWV3aHdseTQ5d2liY2Z4cnVkdzg5YmZubyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/qPuhFBQt8xLEY/giphy.gif'"\
           "width=400>"


@app.route("/<int:guess>")
def user_guess(guess):
    if number != guess:
        result = "high" if number < guess else "low"
        return f"<h1 style='color: {random.choice(COLOURS)}'>Too {result}, try harder!</h1>" \
                f"<img src='{random.choice(SAD_PUPPIES)}'>"
    return f"<h1 style='color: green'>You got it right!!!</h1>" \
            f"<img src='https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmU1Zm9oZmMxaDBmaGdmeTFlb2lyZ3dyNnNycXA5aXpkbmhpZXJsNCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l2uluGTvB7DAQvZyHp/giphy.gif'"\
            "width=400>"


if __name__ == "__main__":
    app.run(debug=True)
