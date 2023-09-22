class OBitStream():
	'''
	Little endian binary output stream,
	represents data in bit as string
	'''
	def __init__(self):
		self._v = ''

	def __str__(self):
		return self._v

	def __len__(self):
		return len(self._v)

	def getByteList(self):
		# self._v.chunk(8).map(reversed).map(int(_, 2))
		def chunk(s, n):
			return [s[i:i+8] for i in range(0, len(self._v), n)]

		return [int(bits[::-1], 2) for bits in chunk(self._v, 8)]

	def toHexString(self):
		return ' '.join(map('{0:02x}'.format, self.getByteList()))

	def append(self, value, num_bits):
		if num_bits == 0:
			return

		if num_bits < 0 or num_bits > 32:
			raise ValueError('[0, 32] bits only')

		self._v += '{0:032b}'.format(value)[::-1][:num_bits]

	def appendString(self, str_value):
		for v in str_value:
			self._v += ('{0:08b}'.format(ord(v)))[::-1]

	def writeBytes(self, writer):
		writer.write(bytearray(self.getByteList()))

