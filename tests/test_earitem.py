import unittest
import os

from lib import EarItem
from lib import OBitStream
from . import FILE_ROOT_DIR

class MemStream():
	def __init__(self):
		self._v = ""

	def __str__(self):
		r = []
		for i in xrange(0, len(self._v), 8):
			bits = self._v[i:i+8][::-1]
			r.append(int(bits, 2))

		return ' '.join(map('{0:02x}'.format, r))

	def append(self, value, num_bits):
		format_str = '{0:0' + str(num_bits) + 'b}'
		mask = 0xFFFFFFFF >> (32 - num_bits)
		# print('mask:{0:0b}, bits:{1}'.format(mask, num_bits))
		bits = format_str.format(value & mask)

		self._v += bits[::-1]

class TestEarItem(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()


	def test_short_name(self):
		self.item = EarItem("Simon")
		self.item.writeStream(self.s)
		b = self.s.getByteList()
		self.assertEquals("JM\x10\x00\xa1", ''.join(map(chr, b[:5])))

		with open(os.path.join(FILE_ROOT_DIR, "[Ear]Simon.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_over_long_name(self):
		self.assertRaises(ValueError, EarItem, "NoNameHasNoName")
