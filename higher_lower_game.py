from flask import Flask, render_template
from decorators import *
from random import randint

# app = Flask(__name__, static_folder='static', template_folder='template')
app = Flask(__name__)

chosen_num = randint(0, 9)

@app.route("/")
@make_heading
def hello_world():
    return "<center>Guess a Number between 0 and 9</center>"
    # return render_template('template.html')


@app.route("/<int:given_num>")
# @make_heading
def check_value(given_num):
    if given_num == chosen_num:
        return ("<p style='color: green; text-align: center;'>Congratulations. You have found the correct number!</p><br>"
                "<img style='display: block; margin-left: auto; margin-right: auto;' src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='350' height='500'></img>")
    elif given_num < chosen_num:
        return ("<p style='color: red; text-align: center;'>Too low. Try again.</p><br>"
                "<img style='display: block; margin-left: auto; margin-right: auto;' src = 'https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='500' height='500'></img>")
    else:
        return ("<p style='color: red; text-align: center;'>Too High. Try again.</p><br>"
                "<img style='display: block; margin-left: auto; margin-right: auto;' src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='500' height='500'></img>")

if __name__ == "__main__":
    app.run(debug=True)
