from jar import Jar
import pytest

def test_init():
	jar = Jar(10,1)
	assert jar.capacity == 10
	assert jar.size == 1

def test_def_cap():
	jar = Jar()
	assert jar.capacity == 12
	with pytest.raises(ValueError):
		assert Jar(-10)

def test_size():
	with pytest.raises(ValueError):
		assert Jar(12,-12)

def test_dep():
	jar = Jar()
	jar.deposit(1)
	assert jar.size == 1

def test_with():
	jar = Jar(12,1)
	jar.withdraw(1)
	assert jar.size == 0

def test_str():
	jar = Jar(1,1)
	assert str(jar) == '🍪'

