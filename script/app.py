from flask import Flask, render_template, jsonify, request, redirect
from .Game import create_game

from flask import Flask, render_template, session
from .Game import create_game
import os
from copy import deepcopy


class NimFlask:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = os.environ.get(
            "SECRET_KEY", "dev-key-if-missing")

        self.rounting()

    def get_game(self):
        if not "mounts" in session:
            game = create_game(player_type=session["player_type_turn"],
                               player_names=session["player_names"])
            session["initial_mounts"] = deepcopy(game.mounts)
            session["initial_turn"] = game.currentPlayerNum
            session["player_type_turn"] = game.get_player_type()
            return game
        else:
            return create_game(mounts=session.get("mounts", None),
                               currentPlayerNum=session.get("turn", None),
                               player_type=session["player_type_turn"],
                               player_names=session["player_names"])

    def save_game(self, game):
        session["mounts"] = game.mounts
        session["turn"] = game.currentPlayerNum

    def rounting(self):

        @self.app.route("/healthcheck")
        def healthcheck():

            return "OK", 200

        @self.app.route("/")
        def init():

            return render_template("start.html")

        @self.app.route("/start", methods=["POST"])
        def start():
            mode = request.form.get("mode")  # pvp or pvc
            first_mode = request.form.get("first_mode")  # random or manual

            # プレイヤー種別
            if mode == "pvp":
                player_type = ["Human", "Human"]
                name1 = request.form.get("name1") or "プレイヤー1"
                name2 = request.form.get("name2") or "プレイヤー2"
            else:
                player_type = ["Human", "CP"]
                name1 = request.form.get("name1") or "あなた"
                name2 = "コンピュータ"

            player_names = [name1, name2]

            # 先行処理
            if first_mode == "random":
                import random
                if random.random() < 0.5:
                    pass  # そのまま
                else:
                    player_type = player_type[::-1]
                    player_names = player_names[::-1]
            else:
                first = int(request.form.get("first", 0))
                if first == 1:
                    player_type = player_type[::-1]
                    player_names = player_names[::-1]

            session.clear()
            session["player_type_turn"] = player_type
            session["player_names"] = player_names

            return redirect("/play")

        @self.app.route("/play")
        def play():

            return render_template("play.html")

        @self.app.route("/reset", methods=["POST"])
        def reset_state():
            keep_keys = {"player_names", "player_type_turn"}
            for key in list(session.keys()):
                if key not in keep_keys:
                    session.pop(key)

            return jsonify({"success": True, "message": "ゲーム再スタート"})

        @self.app.route("/get_state")
        def get_state():
            game = self.get_game()
            return jsonify({"mounts": game.mounts, "turn": game.currentPlayerNum, "now_player_type": game.player_type_list[game.currentPlayerNum],
                            "now_player_name": session["player_names"][game.currentPlayerNum]})

        @self.app.route("/win")
        def win():
            game = self.get_game()
            winner = f"先行:{session['player_names'][game.currentPlayerNum]}" if game.currentPlayerNum == 1 else f"後攻:{session['player_names'][game.currentPlayerNum]}"
            return render_template("win.html", winner=winner)

        @self.app.route("/move", methods=["POST"])
        def move():
            game = self.get_game()
            win = False
            now_player_num = game.currentPlayerNum
            now_player_type = game.player_type_list[now_player_num]

            # 入力値取得
            if now_player_type == "CP":
                player = game.player1 if now_player_num == 0 else game.player2
                index, amount = player.select_move(game.mounts)
            else:
                data = request.get_json()
                index = data.get("index")
                amount = data.get("amount")
            print(f"index:{index}")
            print(f"amoutn:{amount}")
            # バリデーション
            if not (isinstance(index, int) and isinstance(amount, int)):
                return jsonify({"success": False, "message": "入力が正しくない"})
            if not (0 <= index < len(game.mounts)):
                return jsonify({"success": False, "message": "その山はありません"})
            if not (1 <= amount <= game.mounts[index]):
                return jsonify({"success": False, "message": "その量はとれませんよ"})

            # 状態更新
            game.mounts[index] -= amount
            win = game.GameWin()
            if not win:
                game.currentPlayerNum ^= 1

            self.save_game(game)

            return jsonify({
                "success": True,
                "mounts": game.mounts,
                "now_player_type": game.player_type_list[game.currentPlayerNum],
                "message": f"山{index}から{amount}とりました",
                "win": win,
                "turn": game.currentPlayerNum
            })

    def run(self):
        self.app.run(debug=True, port=6225)


NimServer = NimFlask()
app = NimServer.app

if __name__ == "__main__":
    NimServer.run()
