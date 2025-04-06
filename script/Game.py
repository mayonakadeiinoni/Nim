from Player import *


class NimGame:

    def __init__(self, mounts, player1, player2):
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

    def Play(self):
        count = 0
        self.MountDisplay()
        while (True):
            if count == 0:
                index, amount = self.player1.select_move(self.mounts)
            else:
                index, amount = self.player2.select_move(self.mounts)

            self.mounts[index] -= amount
            self.MountDisplay()
            if self.isGameEnd():
                print(f"プレイヤー：{count}が勝ちです．")
                break
            count += 1
            count %= 2


if __name__ == "__main__":
    player1 = HumanPlayer("人間")
    player2 = ComputerPlayer("CP")
    mounts = [5, 8, 4]
    Game = NimGame(mounts, player1, player2)
    Game.Play()
