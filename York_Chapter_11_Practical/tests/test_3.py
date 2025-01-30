from York_Chapter_11_Practical.src.TIY import York_TIY_5_3
import importlib

def test_alien_color_green(capsys):
    importlib.reload(York_TIY_5_3)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[0] == "Player earned 5 points!"

def test_alien_color_yellow(capsys):
    importlib.reload(York_TIY_5_3)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[1] == "Player earned 5 points!"