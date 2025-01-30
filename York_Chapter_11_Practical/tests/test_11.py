from York_Chapter_11_Practical.src.TIY import York_TIY_5_11
import importlib

from York_Chapter_11_Practical.src.TIY.York_TIY_5_11 import list, list2

new_list = []


def test_naming_num(capsys):
    importlib.reload(York_TIY_5_11)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    for count, num in enumerate(list):
        if num == 1:
            assert "1st" in lines[count]
            new_list.append("1st")
        elif num == 2:
            assert "2nd" in lines[count]
            new_list.append("2nd")
        elif num == 3:
            assert "3rd" in lines[count]
            new_list.append("3rd")
        else:
            assert f"{num}th" in lines[count]
            new_list.append(f"{num}th")

length = len(list)

def test_naming_num_comprehension(capsys):
    assert new_list == list2
