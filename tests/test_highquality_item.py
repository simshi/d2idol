import unittest

from lib import OBitStream
from lib.highquality_item import HighQualityItem

class TestHighQualityItem(unittest.TestCase):
	def setUp(self):
		self.stream = OBitStream()

	def test_initialization_defaults(self):
		item = HighQualityItem()
		self.assertEqual(item.code, "amu ")
		self.assertEqual(item.iLevel, 88)

	def test_initialization_custom_code(self):
		item = HighQualityItem("rin ")
		self.assertEqual(item.code, "rin ")

	def test_initialization_custom_sockets(self):
		item = HighQualityItem("rin ", 4)
		self.assertEqual(item.guid, 0x04030211 * 4)

	def test_initialization_custom_subtype(self):
		item = HighQualityItem("rin ", 4, 3)
		self.assertEqual(item.subType, 3)

	def test_add_prop(self):
		item = HighQualityItem()
		item.addProp(0, 10)
		self.assertEqual(len(item.props), 1)

	def test_add_multiple_props(self):
		item = HighQualityItem()
		item.addProp(0, 10)
		item.addProp(1, 20)
		self.assertEqual(len(item.props), 2)

	def test_write_stream(self):
		item = HighQualityItem()
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_props(self):
		item = HighQualityItem()
		item.addProp(0, 10)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_sockets(self):
		item = HighQualityItem("rin ", 4)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_header(self):
		item = HighQualityItem()
		item.writeStream(self.stream)
		s = str(self.stream)
		self.assertGreater(len(s), 0)
