from numb3rs import validate


def test_num():
    assert validate('1') == False
    assert validate('1.1') == False
    assert validate('1.1.1') == False

def test_home():
    assert validate('127.0.0.1') == True

def test_max_true():
    assert validate('255.255.255.255') == True

def test_least_true():
    assert validate('0.0.0.0') == True

def test_over():
    assert validate('1.1.1.1') == True
    assert validate('1.1.1.1000') == False
    assert validate('1.1.1000.1') == False
    assert validate('1.1000.1.1') == False
    assert validate('276.1.1.1') == False
    assert validate('1.300.275.263') == False

def test_string():
    assert validate('cat') == False

def test_first_byte():
        assert validate("1.1000.1.1") == False


