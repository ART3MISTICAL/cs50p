from seasons import convert
import pytest

def test_one():
	assert convert('2021-6-7') == 'Five hundred twenty-five thousand, six hundred minutes'

def test_two():
	assert convert('2020-6-7') == 'One million, fifty-one thousand, two hundred minutes'

def test_invalid():
	with pytest.raises(SystemExit):
		assert convert('Feb 1, 2020')