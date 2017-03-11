import unittest

from lib import OBitStream

class MemWriter():
	def __init__(self):
		self.buf = bytearray()

	def write(self, bytes):
		self.buf.extend(bytes)

	def __str__(self):
		return ' '.join(map('{0:02x}'.format, self.buf))

class TestOBitStream(unittest.TestCase):
	def setUp(self):
		self.stream = OBitStream()


	def test_append_empty(self):
		self.assertEquals('', str(self.stream))
		self.assertEquals('', self.stream.toHexString())

	def test_append_zero_bit(self):
		self.stream.append(0xf, 0)
		self.assertEquals('', str(self.stream))
		self.assertEquals('', self.stream.toHexString())

	def test_append_one_bit(self):
		self.stream.append(1, 1)
		self.assertEquals('1', str(self.stream))
		self.assertEquals('01', self.stream.toHexString())

	def test_append_one_bit_extracted(self):
		self.stream.append(0xf, 1)
		self.assertEquals('1', str(self.stream))
		self.assertEquals('01', self.stream.toHexString())

	def test_append_8_bits(self):
		self.stream.append(0x76, 8)
		self.assertEquals('01110110'[::-1], str(self.stream))
		self.assertEquals('76', self.stream.toHexString())

	def test_append_9_bits(self):
		self.stream.append(0x176, 9)
		self.assertEquals('101110110'[::-1], str(self.stream))
		self.assertEquals('76 01', self.stream.toHexString())

	def test_append_9_bits_extracted(self):
		self.stream.append(0x776, 9)
		self.assertEquals('101110110'[::-1], str(self.stream))
		self.assertEquals('76 01', self.stream.toHexString())

	def test_append_32bits(self):
		self.stream.append(0x1F1F2F4F8, 32)
		self.assertEquals('11110001111100101111010011111000'[::-1], str(self.stream))
		self.assertEquals('f8 f4 f2 f1', self.stream.toHexString())

	def test_append_3_2(self):
		self.stream.append(3, 3)
		self.stream.append(1, 2)
		self.assertEquals('01011'[::-1], str(self.stream))
		self.assertEquals('0b', self.stream.toHexString())

	def test_append_3_6_4(self):
		self.stream.append(int('001', 2), 3)
		self.stream.append(int('000011', 2), 6)
		self.stream.append(int('0111', 2), 4)
		self.assertEquals('0111000011001'[::-1], str(self.stream))
		self.assertEquals('19 0e', self.stream.toHexString())

	def test_append_string(self):
		self.stream.appendString("012 ")
		self.assertEquals('30 31 32 20', self.stream.toHexString())
		w = MemWriter()
		self.stream.writeBytes(w)
		self.assertEquals('30 31 32 20', str(w))


	def test_write_bytes(self):
		self.stream.append(int('1110101', 2), 7)
		self.assertEquals('75', self.stream.toHexString())
		w = MemWriter()
		self.stream.writeBytes(w)
		self.assertEquals('75', str(w))

	def test_write_bytes_long(self):
		self.stream.append(int('10100001111', 2), 11)
		self.assertEquals('0f 05', self.stream.toHexString())
		w = MemWriter()
		self.stream.writeBytes(w)
		self.assertEquals('0f 05', str(w))
