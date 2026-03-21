import unittest

from lib import OBitStream
from lib import quality
from lib.setitem import SetItem
from lib.quality_item import QualityItem
from lib.itemprops import ItemProps

class TestSetItem(unittest.TestCase):
	def setUp(self):
		self.stream = OBitStream()

	def test_initialization_defaults(self):
		item = SetItem()
		self.assertEqual(item.code, "7ws ")
		self.assertEqual(item.itemId, 0x53)

	def test_initialization_custom_code(self):
		item = SetItem("hgl ")
		self.assertEqual(item.code, "hgl ")

	def test_initialization_custom_item_id(self):
		item = SetItem("hgl ", 0x23)
		self.assertEqual(item.itemId, 0x23)

	def test_quality_is_part_of_set(self):
		item = SetItem()
		self.assertEqual(item.qualityVal, quality.PartOfSet)

	def test_inherits_quality_item(self):
		item = SetItem()
		self.assertIsInstance(item, QualityItem)

	def test_default_guid(self):
		item = SetItem()
		self.assertEqual(item.guid, 0x0000ff00)

	def test_set_props_initialization(self):
		item = SetItem()
		self.assertEqual(len(item.setProps), 5)
		for prop in item.setProps:
			self.assertIsInstance(prop, ItemProps)

	def test_add_set_prop(self):
		item = SetItem()
		item.addSetProp(0, 0, 10)
		self.assertEqual(len(item.setProps[0]), 1)

	def test_add_set_prop_different_levels(self):
		item = SetItem()
		item.addSetProp(0, 0, 10)
		item.addSetProp(1, 0, 20)
		item.addSetProp(2, 0, 30)
		self.assertEqual(len(item.setProps[0]), 1)
		self.assertEqual(len(item.setProps[1]), 1)
		self.assertEqual(len(item.setProps[2]), 1)

	def test_write_stream(self):
		item = SetItem()
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_props(self):
		item = SetItem()
		item.addProp(0, 10)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_set_props(self):
		item = SetItem()
		item.addSetProp(0, 0, 10)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_header(self):
		item = SetItem()
		item.writeStream(self.stream)
		s = str(self.stream)
		self.assertGreater(len(s), 0)

	def test_write_extra_data(self):
		item = SetItem()
		item.addSetProp(0, 0, 10)
		item._writeExtraData(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_extra_data_empty(self):
		item = SetItem()
		item._writeExtraData(self.stream)
		self.assertEqual(len(self.stream), 5)

	def test_add_prop(self):
		item = SetItem()
		item.addProp(0, 10)
		self.assertEqual(len(item.props), 1)

	def test_add_prop_group(self):
		item = SetItem()
		item.addPropGroup("characteristic")
		self.assertGreater(len(item.props), 0)
