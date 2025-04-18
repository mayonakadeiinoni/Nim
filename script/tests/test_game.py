# fmt: off
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")))
print(sys.path)
import pytest
from script.Game import NimGame  # your_module を実際のファイル名に置き換えて！
from script.Player import HumanPlayer, ComputerPlayer
# fmt: on


def test_gamewin():
    mounts = [[0, 0, 0], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    corrects = [True, False, False, False]
    for mount, correct in zip(mounts, corrects):
        game = NimGame(mount)
        assert game.GameWin() == correct


def test_get_player_type():
    player_pairs = [[HumanPlayer("player1"), HumanPlayer("player1")],
                    [ComputerPlayer("player1"), HumanPlayer("player1")],
                    [HumanPlayer("player1"), ComputerPlayer("player1")],
                    [ComputerPlayer("player1"), ComputerPlayer("player1")]]
    corrects = [["Human", "Human"],
                ["CP", "Human"],
                ["Human", "CP"],
                ["CP", "CP"],
                ]
    for player_pair, correct in zip(player_pairs, corrects):
        player_type_pair = NimGame([0, 0, 5], player_pair[0], player_pair[1],
                                   currentPlayerNum=0).get_player_type()
        assert player_type_pair == correct


def test_MountAssert():
    game = NimGame([1, 5, 4])
    indexs = [-1, 0, 1, 2, 8, 2]
    amounts = [0, 1, 2, 2, 5, -5]
    corrects = [False, True, True, True, False, False]
    for index, amount, correct in zip(indexs, amounts, corrects):
        assert game.MountAssert(index, amount) == correct


def test_Play_Computer():
    player1 = ComputerPlayer("CP")
    player2 = ComputerPlayer("CP")

    for _ in range(0, 10):
        game = NimGame([10, 5, 4], player1, player2)
        game.Play()
