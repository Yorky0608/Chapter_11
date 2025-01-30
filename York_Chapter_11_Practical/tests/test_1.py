from York_Chapter_11_Practical.src.TIY import York_TIY_5_1
import importlib


def test_fruits1(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[1] == "True"

def test_fruits2(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[3] == "False"

def test_test1(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[5] == "True"

def test_test2(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[7] == "False"

def test_test3(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[9] == "True"

def test_test4(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[11] == "False"

def test_test5(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[13] == "True"

def test_test6(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[15] == "False"

def test_test7(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[17] == "True"

def test_test8(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[19] == "False"

def test_test9(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[21] == "True"

def test_test10(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[23] == "False"

def test_test11(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[25] == "True"

def test_test12(capsys):
    importlib.reload(York_TIY_5_1)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()
    assert lines[27] == "False"
