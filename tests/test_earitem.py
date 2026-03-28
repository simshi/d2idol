import unittest

from lib import EarItem
from lib import OBitStream


class TestEarItem(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()

	def test_short_name(self):
		item = EarItem("Simon")
		item.writeStream(self.s)
		b = self.s.getByteList()
		self.assertEqual("JM\x10\x00\xa1", ''.join(map(chr, b[:5])))

	def test_over_long_name(self):
		self.assertRaises(ValueError, EarItem, "NoNameHasNoName")

	def test_name_max_length(self):
		item = EarItem("1234567890")
		item.writeStream(self.s)
		self.assertGreater(len(self.s), 0)

	def test_name_exactly_11_chars_raises(self):
		self.assertRaises(ValueError, EarItem, "12345678901")

	def test_empty_name(self):
		item = EarItem("")
		item.writeStream(self.s)
		self.assertGreater(len(self.s), 0)

	def test_custom_level(self):
		item = EarItem("Test", iLevel=99)
		item.writeStream(self.s)
		self.assertGreater(len(self.s), 0)

	def test_custom_class(self):
		item = EarItem("Test", iClass=5)
		item.writeStream(self.s)
		self.assertGreater(len(self.s), 0)
