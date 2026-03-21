import unittest

from lib import OBitStream
from lib.charm import Charm

class TestCharm(unittest.TestCase):
	def setUp(self):
		self.stream = OBitStream()

	def test_initialization_defaults(self):
		item = Charm()
		self.assertEqual(item.code, "cm1 ")
		self.assertEqual(item.wSuffix, 0x115)

	def test_initialization_custom_code(self):
		item = Charm("cm2 ")
		self.assertEqual(item.code, "cm2 ")

	def test_initialization_custom_suffix(self):
		item = Charm("cm2 ", 0x116)
		self.assertEqual(item.wSuffix, 0x116)

	def test_set_gfx(self):
		item = Charm()
		item.setGfx(1)
		self.assertTrue(item.bVarGfx)
		self.assertEqual(item.iVarGfx, 1)

	def test_set_gfx_different_values(self):
		item = Charm()
		item.setGfx(5)
		self.assertEqual(item.iVarGfx, 5)

	def test_add_prop(self):
		item = Charm()
		item.addProp(0, 10)
		self.assertEqual(len(item.props), 1)

	def test_add_multiple_props(self):
		item = Charm()
		item.addProp(0, 10)
		item.addProp(1, 20)
		self.assertEqual(len(item.props), 2)

	def test_write_stream(self):
		item = Charm()
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_props(self):
		item = Charm()
		item.addProp(0, 10)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_with_gfx(self):
		item = Charm()
		item.setGfx(1)
		item.writeStream(self.stream)
		self.assertGreater(len(self.stream), 0)

	def test_write_stream_header(self):
		item = Charm()
		item.writeStream(self.stream)
		s = str(self.stream)
		self.assertGreater(len(s), 0)
