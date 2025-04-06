import random


class Player:
    """プレイヤーを表す親クラス．

    Attributes:
        name (str): プレイヤーを表す名前

    """

    def __init__(self, name):
        self.name = name

    def select_move(self, piles):
        raise NotImplementedError(
            "This method should be overridden by subclasses")


class HumanPlayer(Player):

    """Playerを継承するクラス．

    人間が操作するプレイヤーを表すクラスです．
    Attributes:
        name (str): プレイヤーを表す名前(継承)
    """

    def select_move(self, mount):
        index = int(input("どの山からとるか"))
        amount = int(input("山からとる量"))
        return index, amount


class ComputerPlayer(Player):

    """Playerを継承するクラス．

    コンピュータが操作するプレイヤーを表すクラスです．
    Attributes:
        name (str): プレイヤーを表す名前(継承)
    """

    def select_move(self, mount):
        # まだ操作は未定．
        valid_indexs = [i for i, pile in enumerate(mount) if pile > 0]
        index = random.choice(valid_indexs)
        amount = random.randint(1, mount[index])
        print(f"\n\n選んだ番号：{index}")
        print(f"山の量：{amount}")
        return index, amount
