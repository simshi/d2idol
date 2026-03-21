import unittest

from lib import OBitStream
from lib import quality
from lib.uniqitem import UniqItem
from lib.quality_item import QualityItem

class TestUniqItem(unittest.TestCase):
	def setUp(self):
		self.stream = OBitStream()

	def test_initialization_defaults(self):
		item = UniqItem()
		self.assertEqual(item.code, "amu ")
		self.assertEqual(item.itemId, 25)

	def test_initialization_custom_code(self):
		item = UniqItem("rin ")
		self.assertEqual(item.code, "rin ")

	def test_initialization_custom_item_id(self):
		item = UniqItem("rin ", 0x78)
		self.assertEqual(item.itemId, 0x78)

	def test_quality_is_unique(self):
		item = UniqItem()
		self.assertEqual(item.qualityVal, quality.Unique)

	def test_inherits_quality_item(self):
		item = UniqItem()
		self.assertIsInstance(item, QualityItem)

	def test_default_guid(self):
		item = UniqItem()
		self.assertEqual(item.guid, 0x04030211)

	def test_write_stream(self):
		item = UniqItem()
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_props(self):
		item = UniqItem()
		item.addProp(0, 10)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_header(self):
		item = UniqItem()
		item.writeStream(self.stream)
		s = str(self.stream)
		self.assertGreater(len(s), 0)

	def test_add_prop(self):
		item = UniqItem()
		item.addProp(0, 10)
		self.assertEqual(len(item.props), 1)

	def test_add_multiple_props(self):
		item = UniqItem()
		item.addProp(0, 10)
		item.addProp(1, 20)
		self.assertEqual(len(item.props), 2)

	def test_add_prop_group(self):
		item = UniqItem()
		item.addPropGroup("characteristic")
		self.assertGreater(len(item.props), 0)
