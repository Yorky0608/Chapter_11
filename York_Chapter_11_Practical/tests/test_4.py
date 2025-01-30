from York_Chapter_11_Practical.src.TIY import York_TIY_5_4
import importlib

def test_alien_color(capsys):
    importlib.reload(York_TIY_5_4)  # Reload to capture fresh output
    captured = capsys.readouterr()

    if York_TIY_5_4.alien_color[York_TIY_5_4.random_num] == "green":
        assert captured.out == "Player earned 5 points!\n"
    else:
        assert captured.out == "Player earned 10 points!\n"