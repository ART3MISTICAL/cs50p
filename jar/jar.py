class Jar:
	def __init__(self, capacity = 12, size = 0):
		self.capacity = capacity
		self.size = size

	def __str__(self):
		return '🍪' * self.size

	def deposit(self, n ):
		if (self.size + n) > self.capacity:
			raise ValueError
		else:
			self.size = self.size + n

	def withdraw(self, n):
		if (self.size - n) > self.capacity:
			raise ValueError

		else:
			self.size = self.size - n

	@property
	def capacity(self):
		return self._capacity

	@capacity.setter
	def capacity(self, capacity):
		if capacity < 0:
			raise ValueError
		else:
			self._capacity = capacity

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, size):
		if size < 0:
			raise ValueError
		else:
			self._size = size


def main():
	jar = Jar(10)
	print (jar.capacity)
	jar.deposit(5)
	jar.withdraw(1)
	print (jar.size)
	print (str(jar))

if __name__ == '__main__':
	main()
