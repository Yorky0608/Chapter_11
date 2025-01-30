from York_Chapter_11_Practical.src.TIY import York_TIY_5_6
import importlib

def test_age(capsys):
    importlib.reload(York_TIY_5_6)  # Reload to capture fresh output
    captured = capsys.readouterr()

    assert captured.out == "Person is an adult.\n"