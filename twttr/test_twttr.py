from twttr import shorten

def main():
    test_upper()
    test_lower()
    test_num()
    test_pun()

def test_uppper():
    assert shorten('HELLO') == 'HLL'
    assert shorten('CS50') == 'CS50'
    assert shorten('PYTHON') == 'PYTHN'

def test_lower():
    assert shorten('hello') == 'hll'
    assert shorten('cs50') == 'cs50'
    assert shorten('python') == 'pythn'

def test_num():
    assert shorten('123456') == '123456'

def test_pun():
    assert shorten(".,';") == ".,';"


if __name__ == "__main__":
    main()