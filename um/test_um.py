from um import count

def test_normal():
    assert count('um') == 1
    assert count('hello, um, world')

def test_upper():
    assert count('Um') == 1
    assert count('hello, UM, world') == 1

def test_multiple():
    assert count('um um um') == 3

def test_yum():
    assert count('yum yummy') == 0

def test_space():
    assert count('   um     ') == 1