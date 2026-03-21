import unittest

from lib import OBitStream
from lib import quality
from lib.quality_item import QualityItem

class TestQualityItem(unittest.TestCase):
	def setUp(self):
		self.stream = OBitStream()

	def test_initialization_defaults(self):
		item = QualityItem("amu ", quality.Unique, 25)
		self.assertEqual(item.code, "amu ")
		self.assertEqual(item.qualityVal, quality.Unique)
		self.assertEqual(item.itemId, 25)

	def test_initialization_with_guid(self):
		item = QualityItem("amu ", quality.Unique, 25, guid=0x123)
		self.assertEqual(item.guid, 0x123)

	def test_default_values(self):
		item = QualityItem("amu ", quality.Unique, 25)
		self.assertEqual(item.nGems, 0)
		self.assertEqual(item.bClass, 0)
		self.assertEqual(item.wClass, 1)

	def test_add_prop(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item.addProp(0, 10)
		self.assertEqual(len(item.props), 1)

	def test_add_multiple_props(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item.addProp(0, 10)
		item.addProp(1, 20)
		self.assertEqual(len(item.props), 2)

	def test_add_prop_group(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item.addPropGroup("characteristic")
		self.assertGreater(len(item.props), 0)

	def test_write_stream(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_header(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item.writeStream(self.stream)
		s = str(self.stream)
		self.assertGreater(len(s), 0)

	def test_write_extra_data_hook(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item._writeExtraData(self.stream)
		self.assertEqual(len(self.stream), 0)

	def test_write_extra_props_hook(self):
		item = QualityItem("amu ", quality.Unique, 25)
		item._writeExtraProps(self.stream)
		self.assertEqual(len(self.stream), 0)

	def test_quality_part_of_set(self):
		item = QualityItem("7ws ", quality.PartOfSet, 0x53)
		self.assertEqual(item.qualityVal, quality.PartOfSet)

	def test_quality_unique(self):
		item = QualityItem("amu ", quality.Unique, 25)
		self.assertEqual(item.qualityVal, quality.Unique)
