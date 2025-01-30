from York_Chapter_11_Practical.src.TIY import York_TIY_5_8
import importlib

def test_usernames(capsys):
    importlib.reload(York_TIY_5_8)
    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert "Hello Yorkshire06, nice to see you again." in lines[0]
    assert "Hello MyNsmes, nice to see you again." in lines[1]
    assert "Hello Popeletvt, nice to see you again." in lines[2]
    assert "Hello qwertyuiop[], nice to see you again." in lines[3]
    assert "Hello 1qaz2wsx, nice to see you again." in lines[4]
    assert "Welcome admin, would you like to see the logs?" in lines[5]