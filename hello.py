import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
from othello import *
from random import choice, choices

app = Flask(__name__, static_folder='static', template_folder='template')

with open("static/hobbies.json") as file:
    hobbies = json.load(file).get('hobbies')


@app.route("/")
def welcome_page():
    global blogs
    year = datetime.now().year
    return render_template("blog_index.html", hobbies=hobbies, year=year)


@app.route("/hobby/<int:num>")
def display_hobby(num):
    if 1 <= num <= len(hobbies):
        year = datetime.now().year
        return render_template("post.html", hobby=hobbies[num - 1], year=year)
    return


@app.route("/hobby/<int:num>/images", methods=["POST"])
def return_images(num):
    global hobbies
    if 1 <= num <= len(hobbies):
        return jsonify({"imagePaths": ",".join(hobbies[num - 1].get("imagePaths")), "alts": ",".join(hobbies[num - 1].get("alts"))})
    return


@app.route("/about/images", methods=["POST"])
def return_about_images():
    imagePaths = ["/static/images/CVMUN 2022.jpeg", "/static/images/CVMUN 2023.jpeg", "/static/images/VMUN 2023.jpeg"]
    alts = ["VMUN 2023", "CVMUN 2023", "CVMUN 2022"]
    return jsonify({"imagePaths": ",".join(imagePaths), "alts": ",".join(alts)})


@app.route("/about")
def about():
    year = datetime.now().year
    return render_template("about.html", year=year)


@app.route("/contact_us")
def contact():
    name = "Aditya Neeraje"
    year = datetime.now().year
    return render_template("contact.html", name=name, year=year)


@app.route("/receive_input", methods=["POST"])
def receive_input():
    name = "Aditya Neeraje"
    year = datetime.now().year

    data = request.get_json()
    message = data.get("message", "")
    print(message)

    return render_template("contact.html", name=name, year=year)


states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware', 'Florida',
          'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska',
          'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio',
          'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas',
          'Utah', 'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']
x_coordinates = [69.58620689655173, 22.689655172413794, 22.27586206896552, 58.827586206896555, 11.103448275862071,
                 35.241379310344826, 93.58620689655173, 87.93103448275862, 81.3103448275862, 75.93103448275862,
                 6.96551724137931, 22.27586206896552, 63.37931034482759, 69.3103448275862, 56.206896551724135,
                 47.793103448275865, 70.6896551724138, 60.3448275862069, 94.41379310344827, 89.72413793103448,
                 88.75862068965517, 70.9655172413793, 55.10344827586207, 63.79310344827586, 58.827586206896555,
                 31.379310344827584, 44.758620689655174, 15.655172413793103, 91.93103448275862, 93.72413793103448,
                 33.03448275862069, 84.48275862068965, 81.17241379310344, 44.89655172413793, 75.10344827586206,
                 49.724137931034484, 11.655172413793103, 82.82758620689656, 93.0344827586207, 80.48275862068965,
                 44.89655172413793, 69.03448275862068, 46.13793103448276, 24.482758620689655, 89.86206896551724,
                 83.65517241379311, 13.862068965517246, 78.96551724137932, 61.44827586206897, 32.758620689655174]
y_coordinates = [30.855397148676172, 13.543788187372705, 38.59470468431772, 40.835030549898164, 46.537678207739305,
                 52.85132382892057, 67.31160896130346, 58.55397148676171, 17.413441955193484, 33.91038696537678,
                 20.672097759674134, 70.57026476578412, 55.4989816700611, 57.942973523421585, 62.42362525458248, 50.0,
                 47.759674134419555, 23.523421588594708, 85.84521384928718, 55.4989816700611, 72.81059063136456,
                 68.5336048879837, 77.08757637474542, 27.393075356415476, 46.94501018329939, 80.75356415478615,
                 60.9979633401222, 59.775967413441954, 75.25458248472505, 61.20162932790224, 38.39103869653768,
                 69.14460285132382, 43.686354378818734, 80.95723014256619, 58.55397148676171, 39.81670061099796,
                 76.06924643584522, 62.627291242362524, 64.86761710794298, 38.59470468431772, 70.57026476578412,
                 42.46435845213849, 26.374745417515275, 54.68431771894094, 77.90224032586558, 50.610997963340125,
                 87.27087576374745, 53.66598778004073, 73.0142566191446, 66.90427698574338]
guessed_states = []
score = 0


@app.route("/hobby/states_game")
def play_states_game():
    global score, guessed_states, states, x_coordinates, y_coordinates
    msg = request.args.get('msg', 'start')
    if msg == "hint":
        chosen_state = choice([state for state in states if state not in guessed_states])
        random_indices = choices([index for index in range(len(chosen_state)) if chosen_state[index] != " "],
                                 k=round(len(chosen_state) / 3))
        hint = ''.join(
            [chosen_state[index] if index in random_indices or chosen_state[index] == " " else "*" for index in
             range(len(chosen_state))])
        return render_template("name_the_states.html", states=states, x_coordinates=x_coordinates,
                               y_coordinates=y_coordinates, guessed_states=guessed_states, msg=msg, score=score,
                               hint=hint)
    return render_template("name_the_states.html", states=states, x_coordinates=x_coordinates,
                           y_coordinates=y_coordinates, guessed_states=guessed_states, msg=msg, score=score)


@app.route("/check_state", methods=["POST"])
def check_state():
    global score, guessed_states, states, x_coordinates, y_coordinates

    data = request.get_json()
    message = data.get("message").strip().title()

    if message == "Hint":
        return jsonify({"redirect_path": url_for("play_states_game", msg="hint")})

    if message == "Give Up":
        return jsonify({"redirect_path": url_for("play_states_game", msg="give_up")})

    if message == "Restart":
        guessed_states = []
        score = 0
        return jsonify({"redirect_path": url_for("play_states_game", msg="start")})

    if message in states and message not in guessed_states:
        score += 1
        guessed_states.append(message)

        if score == len(states):
            return jsonify({"redirect_path": url_for("play_states_game", msg="victory")})

        return jsonify({"redirect_path": url_for("play_states_game", msg="normal")})

    if message in guessed_states:
        return jsonify({"redirect_path": url_for("play_states_game", msg="already_guessed")})

    if not message:
        return jsonify({"redirect_path": url_for("play_states_game", msg="blank")})

    if message not in states:
        return jsonify({"redirect_path": url_for("play_states_game", msg="incorrect")})


white_buttons_list = [8 * 3 + 3, 8 * 4 + 4]
black_buttons_list = [8 * 3 + 4, 8 * 4 + 3]
white_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, False)
black_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, True)
black_to_play = True


@app.route('/hobby/othello')
def othello():
    global white_buttons_list, black_buttons_list, white_clickable_buttons, black_clickable_buttons
    return render_template("othello.html", white_buttons_list=white_buttons_list, black_buttons_list=black_buttons_list, white_clickable_buttons=white_clickable_buttons, black_clickable_buttons=black_clickable_buttons)


@app.route('/clicked_button', methods=['POST'])
def check_clicked_button():
    global white_clickable_buttons, black_clickable_buttons, white_buttons_list, black_buttons_list
    data = request.get_json()
    message = int(data.get("message"))
    button_clicked(message, white_buttons_list, black_buttons_list, True)
    white_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, False)
    black_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, True)
    return jsonify({"redirect_path": url_for("othello")})

@app.route('/restart_othello', methods=['POST'])
def restart_othello_game():
    global white_clickable_buttons, black_clickable_buttons, white_buttons_list, black_buttons_list
    white_buttons_list = [8*3+3, 8*4+4]
    black_buttons_list = [8*3+4, 8*4+3]
    white_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, False)
    black_clickable_buttons = clickable_buttons(white_buttons_list, black_buttons_list, True)
    return jsonify({"redirect_path": url_for("othello")})


if __name__ == "__main__":
    app.run(debug=True)
