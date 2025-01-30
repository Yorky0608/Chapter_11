from York_Chapter_11_Practical.src.TIY import York_TIY_5_5
import importlib

def test_alien_color(capsys):
    importlib.reload(York_TIY_5_5)  # Reload to capture fresh output
    captured = capsys.readouterr()

    if York_TIY_5_5.color == "green":
        assert captured.out == "Player earned 5 points!\n"
    elif York_TIY_5_5.color == "yellow":
        assert captured.out == "Player earned 10 points!\n"
    elif York_TIY_5_5.color == "red":
        assert captured.out == "Player earned 15 points!\n"