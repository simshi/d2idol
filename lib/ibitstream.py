class IBitStream():
	'''
	Little endian binary input stream,
	reads data from bytes as bits
	'''
	def __init__(self, data=None):
		self._v = ''
		self._offset = 0
		if data is not None:
			self.setData(data)

	def __str__(self):
		return self._v

	def __len__(self):
		return len(self._v)

	def setData(self, data):
		self._v = ''.join(["{0:08b}".format(b)[::-1] for b in data])
		self._offset = 0

	def getOffset(self):
		return self._offset

	def remaining(self):
		return len(self._v) - self._offset

	def isEnd(self):
		return self._offset >= len(self._v)

	def read(self, num_bits):
		if num_bits == 0:
			return 0

		if num_bits < 0:
			raise ValueError('num_bits must be >= 0')

		if self._offset + num_bits > len(self._v):
			raise ValueError('not enough bits remaining')

		bits = self._v[self._offset:self._offset + num_bits]
		self._offset += num_bits
		return int(bits[::-1], 2)

	def readString(self, length):
		result = ''
		for _ in range(length):
			bits = self._v[self._offset:self._offset + 8]
			self._offset += 8
			result += chr(int(bits[::-1], 2))
		return result

	def peek(self, num_bits):
		if num_bits == 0:
			return 0

		if num_bits < 0:
			raise ValueError('num_bits must be >= 0')

		if self._offset + num_bits > len(self._v):
			raise ValueError('not enough bits remaining')

		bits = self._v[self._offset:self._offset + num_bits]
		return int(bits[::-1], 2)

	def skip(self, num_bits):
		if num_bits < 0:
			raise ValueError('num_bits must be >= 0')

		if self._offset + num_bits > len(self._v):
			raise ValueError('not enough bits remaining')

		self._offset += num_bits
