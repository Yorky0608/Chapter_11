from York_Chapter_11_Practical.src.TIY import York_TIY_5_7
import importlib

def test_fruit1(capsys):
    importlib.reload(York_TIY_5_7)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert "There is an apple in the list." in lines[0]
    assert "There is an apple in the list." in lines[1]
    assert "There is an orange in the list." in lines[2]
    assert f"There is an {York_TIY_5_7.fruit} in the list." in lines[3]