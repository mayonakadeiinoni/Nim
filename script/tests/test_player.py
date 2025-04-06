# fmt: off
from unittest.mock import patch
import sys
import os

sys.path.append(os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")))
import pytest
from script.Player import HumanPlayer, ComputerPlayer  # your_module を実際のファイル名に置き換えて！

# fmt: on
# HumanPlayerのselect_moveのテスト（モックで入力）


def test_human_player_select_move():
    player = HumanPlayer("Test")
    with patch("builtins.input", side_effect=["1", "3"]):
        index, amount = player.select_move([3, 4, 5])
        assert index == 1
        assert amount == 3

# ComputerPlayerのselect_moveのテスト（有効な山を選ぶか）


def test_computer_player_select_move():
    player = ComputerPlayer("CPU")
    mount = [0, 5, 0]

    for _ in range(10):
        index, amount = player.select_move(mount)
        assert index == 1
        assert 1 <= amount <= 5

# ComputerPlayerが空の山しかないとき


def test_computer_player_all_empty():
    player = ComputerPlayer("CPU")
    mount = [0, 0, 0]
    with pytest.raises(IndexError):
        player.select_move(mount)
