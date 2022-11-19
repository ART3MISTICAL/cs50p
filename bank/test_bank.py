from bank import value

def main():
    test_hello()
    test_h()
    test_other()

def test_hello():
    assert value('hello') == 0
    assert value('HELLO') == 0

def test_h():
    assert value('hey') == 20
    assert value('hi') == 20

def test_other():
    assert value('yo') == 100
    assert value('abc') == 100

if __name__ == '__main__':
    main()