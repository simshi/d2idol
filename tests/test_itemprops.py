import unittest

from lib import OBitStream
from lib.itemprops import ItemProps

class TestItemProps(unittest.TestCase):
	def setUp(self):
		self.props = ItemProps()
		self.stream = OBitStream()

	def test_empty_props(self):
		self.assertEqual(len(self.props), 0)

	def test_add_single_prop(self):
		self.props.add(0, 10)
		self.assertEqual(len(self.props), 1)

	def test_add_multiple_props(self):
		self.props.add(0, 10)
		self.props.add(1, 20)
		self.assertEqual(len(self.props), 2)

	def test_add_same_prop_overwrites(self):
		self.props.add(0, 10)
		self.props.add(0, 20)
		self.assertEqual(len(self.props), 1)

	def test_add_non_class_skill(self):
		self.props.add(97, 32, 0xFF)
		self.assertEqual(len(self.props), 1)

	def test_add_multiple_non_class_skills(self):
		self.props.add(97, 32, 0xFF)
		self.props.add(97, 54, 0xFF)
		self.assertEqual(len(self.props), 2)

	def test_add_all_resistance(self):
		self.props.add(39)
		self.props.add(41)
		self.assertEqual(len(self.props), 2)

	def test_add_fire_resistance(self):
		self.props.add(39)
		self.assertEqual(len(self.props), 1)

	def test_add_lightning_resistance(self):
		self.props.add(41)
		self.assertEqual(len(self.props), 1)

	def test_add_cold_resistance(self):
		self.props.add(43)
		self.assertEqual(len(self.props), 1)

	def test_add_poison_resistance(self):
		self.props.add(45)
		self.assertEqual(len(self.props), 1)

	def test_write_stream_empty(self):
		self.props.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_prop(self):
		self.props.add(0, 10)
		self.props.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_multiple_props(self):
		self.props.add(0, 10)
		self.props.add(1, 20)
		self.props.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_terminator(self):
		self.props.writeStream(self.stream)
		s = str(self.stream)
		self.assertTrue(s.endswith('1' * 9))
