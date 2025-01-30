from York_Chapter_11_Practical.src.TIY import York_TIY_5_9
import importlib

def test_usernames(capsys):
    importlib.reload(York_TIY_5_9)
    captured = capsys.readouterr()

    if not York_TIY_5_9.usernames:
        assert captured.out == "Why no users?\n"
    else:
        #"There should be no usernames!"
        assert False