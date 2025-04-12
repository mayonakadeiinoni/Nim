from .Player import *


class NimGame:

    def __init__(self, mounts, player1=None, player2=None):
        self.mounts = mounts
        self.player1 = player1
        self.player2 = player2
        self.currentPlayerNum = 0  # 0 Or1

    def isGameEnd(self):
        return self.GameWin()

    def GameWin(self):
        return all(mount == 0 for mount in self.mounts)

    def MountDisplay(self):
        for index, mount in enumerate(self.mounts):
            print(f"山：{index}の残り：{mount}")

    def MountAssert(self, index, amount):

        if not (0 <= index <= len(self.mounts)):
            print("山の番号に入ってないです")
            return False
        elif not (0 < amount <= self.mounts[index]):
            print("該当の山の量を超えてます．")
            return False
        return True

    def Opening(self):
        print("########################GAMESTART####################")
        print("これはNimゲームです．\n各プレイヤーは山の任意の番号の任意の量を交互に取ります．")
        print("先にすべての山をゼロにしてしまったプレイヤーが負けです!!")

    def Play(self):
        turn = 0
        self.Opening()
        self.MountDisplay()
        while (True):
            current_player = self.player1 if turn == 0 else self.player2
            print(f"プレイヤー：{current_player.name}\n")
            index, amount = current_player.select_move(self.mounts)

            if not self.MountAssert(index, amount):
                continue
            self.mounts[index] -= amount
            self.MountDisplay()
            if self.isGameEnd():
                print(f"プレイヤー：{current_player.name}が勝ちです．")
                break
            turn += 1
            turn %= 2


def create_game():
    player1 = HumanPlayer("人間")
    player2 = ComputerPlayer("CP")
    mounts = [5, 8, 4]
    Game = NimGame(mounts, player1, player2)
    return Game


if __name__ == "__main__":
    player1 = HumanPlayer("人間")
    player2 = ComputerPlayer("CP")
    mounts = [5, 8, 4]
    Game = NimGame(mounts, player1, player2)
    Game.Play()
