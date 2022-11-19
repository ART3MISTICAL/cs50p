from working import convert
import pytest

def test_str():
    assert convert("5:00 AM to 9:00 PM") == "05:00 to 21:00"
    with pytest.raises(ValueError):
        assert convert('this is cs50')


def test_range():
    assert convert("7 PM to 8 PM") == "19:00 to 20:00"
    with pytest.raises(ValueError):
        assert convert('9:60 AM to 10:70 PM')

def test_char():
    assert convert("7 AM to 8 PM") == "07:00 to 20:00"
    with pytest.raises(ValueError):
        assert convert('9 AM - 9 PM')
