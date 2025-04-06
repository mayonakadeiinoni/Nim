class Player:
    """プレイヤーを表す親クラス．
    
    Attributes:
        name (str): プレイヤーを表す名前
    
    """
    def __init__(self,name):
        self.name=name

    def select_move(self,piles):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class HumanPlayer(Player):
    
    """Playerを継承するクラス．
    
    人間が操作するプレイヤーを表すクラスです．
    Attributes:
        name (str): プレイヤーを表す名前(継承)
    """
    def select_move(self,mount):
        index = int(input("どの山からとるか"))
        amount= int(input("山からとる量"))
        return index,amount

class ComputerPlayer(Player):
    
    """Playerを継承するクラス．
    
    コンピュータが操作するプレイヤーを表すクラスです．
    Attributes:
        name (str): プレイヤーを表す名前(継承)
    """
    def select_move(self,mount):
        ## まだ操作は未定．
        index = int(0)
        amount= int(0)
        return index,amount
