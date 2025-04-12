from flask import Flask, render_template, jsonify, request
from Game import create_game

from flask import Flask, render_template
from Game import create_game
app = Flask(__name__)
game = create_game()


@app.route("/")
def play():
    return render_template("index.html")


@app.route("/get_state")
def get_state():
    return jsonify({"mounts": game.mounts})


if __name__ == "__main__":
    app.run(debug=True, port=5012)
