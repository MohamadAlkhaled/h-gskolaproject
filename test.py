import main


def test_add():
    assert main.add(3,2)==5
    assert main.add(4.5, 4) ==7


def test_sentence():
    assert main.test_sentence('apple') == 'Apple.'
    assert main.test_sentence('Apple') == 'Apple.'


