from flask import Flask, render_template, jsonify, request
from .Game import create_game

from flask import Flask, render_template
from .Game import create_game
app = Flask(__name__)
game = create_game()


@app.route("/")
def play():
    return render_template("index.html")


@app.route("/get_state")
def get_state():
    return jsonify({"mounts": game.mounts, "turn": game.currentPlayerNum})


@app.route("/win")
def win():
    winner = "先行" if game.currentPlayerNum == 1 else "後攻"
    return render_template("win.html", winner=winner)


@app.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    index = data.get("index")
    amount = data.get("amount")
    win = False

    # validation
    if not (isinstance(index, int) and isinstance(index, int)):
        return jsonify({"success": False, "message": "入力が正しくない"})
    if not (0 <= index <= len(game.mounts)):
        return jsonify({"success": False, "message": "その山はありません"})
    if not (1 <= amount <= game.mounts[index]):
        return jsonify({"success": False, "message": "その量はとれませんよ"})

    # 状態更新
    game.mounts[index] -= amount
    print(game.currentPlayerNum)
    game.currentPlayerNum += game.currentPlayerNum
    game.currentPlayerNum = game.currentPlayerNum ^ 1
    print(game.mounts)  # success
    print(game.currentPlayerNum)

    ##
    if game.GameWin:
        win = True
    return jsonify({
        "success": True,
        "mounts": game.mounts,
        "message": f"山{index}から{amount}とりました",
        "win": win
    })


if __name__ == "__main__":
    app.run(debug=True, port=6025)
