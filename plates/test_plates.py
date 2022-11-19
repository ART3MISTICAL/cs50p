from plates import is_valid

def main():
    test_char()
    test_num()
    test_num_mid()
    test_zero()
    test_pun()

def test_char():
    assert is_valid('TT') == True
    assert is_valid('SSSSSS') == True
    assert is_valid('EEEEEEEE') == False
    assert is_valid('O') == False

def test_num():
    assert is_valid('T2') == False
    assert is_valid('2T') == False
    assert is_valid('12') == False

def test_num_mid():
    assert is_valid('ABC123') == True
    assert is_valid('ABC12D') == False

def test_zero():
    assert is_valid('CS05') == False

def test_pun():
    assert is_valid('ABC,12') == False

if __name__ == '__main__':
    main()