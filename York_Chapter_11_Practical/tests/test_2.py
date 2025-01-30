from York_Chapter_11_Practical.src.TIY import York_TIY_5_2
import importlib

def test_t_f1(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[1] == "True"

def test_t_f2(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[3] == "False"

def test_fruits_apple(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[5] == "True"

def test_fruits_pineapple(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[7] == "False"

def test_num1(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[9] == "True"

def test_num2(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[11] == "False"

def test_num3(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[13] == "False"

def test_num4(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[15] == "False"

def test_num5(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[17] == "True"

def test_num6(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[19] == "False"

def test_num7(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[21] == "True"

def test_num8(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[23] == "False"

def test_num9(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[25] == "True"

def test_num10(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[27] == "True"

def test_list1(capsys):
    importlib.reload(York_TIY_5_2)  # Reload to capture fresh output

    captured = capsys.readouterr()
    lines = captured.out.splitlines()

    assert lines[28] == "Carl was in the list."