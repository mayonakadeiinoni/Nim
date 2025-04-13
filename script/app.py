from flask import Flask, render_template, jsonify, request
from .Game import create_game

from flask import Flask, render_template, session
from .Game import create_game


class NimFlask:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = "your-secret-key"  # 適当なランダム文字列
    #    self.game = create_game()

        self.rounting()

    def get_game(self):
        if not "mounts" in session:
            return create_game()
        else:
            return create_game(mounts=session.get("mounts", None),
                               currentPlayerNum=session.get("turn", None))

    def save_game(self, game):
        session["mounts"] = game.mounts
        session["turn"] = game.currentPlayerNum

    def rounting(self):
        @self.app.route("/")
        def play():

            return render_template("index.html")

        @self.app.route("/get_state")
        def get_state():
            game = self.get_game()
            return jsonify({"mounts": game.mounts, "turn": game.currentPlayerNum})

        @self.app.route("/win")
        def win():
            game = self.get_game()
            winner = "先行" if game.currentPlayerNum == 1 else "後攻"
            return render_template("win.html", winner=winner)

        @self.app.route("/move", methods=["POST"])
        def move():
            data = request.get_json()
            index = data.get("index")
            amount = data.get("amount")
            game = self.get_game()
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
            if game.GameWin():
                print(55)
                win = True
            self.save_game(game)
            print(f"win:{win}")

            return jsonify({
                "success": True,
                "mounts": game.mounts,
                "message": f"山{index}から{amount}とりました",
                "win": win
            })

    def run(self):
        self.app.run(debug=True, port=6062)


if __name__ == "__main__":
    NimServer = NimFlask()
    NimServer.run()
