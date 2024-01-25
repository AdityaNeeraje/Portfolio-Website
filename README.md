# Portfolio Website

Hi! My name is Aditya Neeraje. I am a fresher in the CSE Department at IITB. Currently, I'm interested in honing my programming skills and exploring the fields of Reinforcement Learning and Natural Language Processing.

## Table of Contents

- [About](#about)
- [How to Get the Server Running](#getting-started)
- [Usage](#usage)

## About

This website utilizes a HTML, CSS and JavaScript front-end and Flask back-end to create an interactive website, displaying my recent activities in the fields of MUNning/debating, coding up games and competitive programming. In addition, the website links to two flask and javascript-enabled online games I have coded.

## Getting Started

To run the server locally, download (git clone) the repository locally. Opening the folder housing the python code, run the following

```bash
# Installation steps
git clone https://github.com/your-username/your-project.git](https://github.com/AdityaNeeraje/Portfolio-Website)https://github.com/AdityaNeeraje/Portfolio-Website
cd Portfolio-website
sudo apt install python3-flask # If flask is not already installed
export FLASK_APP=hello
export FLASK_ENV=development
pip install –-upgrade Flask Werzeug
flask run


The home page displays the title and intro of my top 3 hobbies, along with a Read More link to take the user to the specific page for each hobby. The home page also links to my Github and Codeforces accounts.

Each hobby page displays a sideshow of images, cycling through images with the image changing every 5s. The home page can be accessed again through either the navbar or the Return to Home buttons. A svg provided the background wave-like graphics.

The navbar also links to two games, a Name the States game and a game of Othello. The Name the States game simulates the Sporcle quiz of the same name. The full name of a state is to be typed in the input box, and the label of the state state is automatically displayed on the map if a valid state is typed. Note that this is case-insensitive. The Hint button gives a partially blanked out state amongst the states not guessed until then. The hint is displayed above the input box, with asterisks representing blanked out characters. Spaces are provided in the appropriate locations for states whose names have multiple words.