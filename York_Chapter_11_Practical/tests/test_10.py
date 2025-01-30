from York_Chapter_11_Practical.src.TIY import York_TIY_5_10
import importlib

from York_Chapter_11_Practical.src.TIY.York_TIY_5_10 import new_users, current_users


def test_usernames(capsys):
    importlib.reload(York_TIY_5_10)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    unused = True
    count = 0

    for new_user in new_users:
        for old_user in current_users:
            if new_user.title() == old_user.title():
                assert (f"Please make another username. {old_user} is already in use."
                        in lines[count])
                unused = False
                break
        if unused:
            assert f"{new_user} is available to use." in lines[count]
        count += 1