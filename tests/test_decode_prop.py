import unittest

from lib import IBitStream, OBitStream
from lib.itemprops import decodeProp


class TestDecodeProp(unittest.TestCase):
	def test_decode_terminator(self):
		stream = IBitStream(bytearray([0xff, 0x01]))
		result = decodeProp(stream)
		self.assertIsNone(result)

	def test_decode_single_raw_prop(self):
		ostream = OBitStream()
		ostream.append(16, 9)
		ostream.append(100, 9)

		stream = IBitStream(bytearray(ostream.getByteList()))
		result = decodeProp(stream)

		self.assertIsNotNone(result)
		self.assertEqual(16, result.id)
		self.assertEqual("+100% Enhanced Defense", result.formatted)
		self.assertEqual(1, len(result.details))

		detail = result.details[0]
		self.assertEqual(9, detail.bits)
		self.assertEqual("raw", detail.ptn)
		self.assertEqual(100, detail.value)

	def test_decode_prop_with_base(self):
		ostream = OBitStream()
		ostream.append(31, 9)
		ostream.append(110, 11)

		stream = IBitStream(bytearray(ostream.getByteList()))
		result = decodeProp(stream)

		self.assertIsNotNone(result)
		self.assertEqual(31, result.id)
		self.assertEqual("+100 Defense", result.formatted)

		detail = result.details[0]
		self.assertEqual(11, detail.bits)
		self.assertEqual("raw", detail.ptn)
		self.assertEqual(110, detail.value)
		self.assertEqual(10, detail.base)

	def test_decode_two_values_prop(self):
		ostream = OBitStream()
		ostream.append(48, 9)
		ostream.append(100, 8)
		ostream.append(200, 9)

		stream = IBitStream(bytearray(ostream.getByteList()))
		result = decodeProp(stream)

		self.assertIsNotNone(result)
		self.assertEqual(48, result.id)
		self.assertEqual("Adds 100-200 fire damage", result.formatted)
		self.assertEqual(2, len(result.details))

		self.assertEqual(100, result.details[0].value)
		self.assertEqual(200, result.details[1].value)

	def test_decode_skill_prop(self):
		ostream = OBitStream()
		ostream.append(97, 9)
		ostream.append(36, 9)
		ostream.append(5, 6)

		stream = IBitStream(bytearray(ostream.getByteList()))
		result = decodeProp(stream)

		self.assertIsNotNone(result)
		self.assertEqual(97, result.id)
		self.assertEqual("Skill Fire Bolt +5", result.formatted)

		detail = result.details[0]
		self.assertEqual("skill", detail.ptn)
		self.assertEqual("Fire Bolt", detail.name)

	def test_decode_multiple_props(self):
		ostream = OBitStream()
		ostream.append(16, 9)
		ostream.append(50, 9)
		ostream.append(19, 9)
		ostream.append(1000, 10)
		ostream.append(0x1ff, 9)

		stream = IBitStream(bytearray(ostream.getByteList()))

		result1 = decodeProp(stream)
		self.assertIsNotNone(result1)
		self.assertEqual(16, result1.id)
		self.assertEqual("+50% Enhanced Defense", result1.formatted)

		result2 = decodeProp(stream)
		self.assertIsNotNone(result2)
		self.assertEqual(19, result2.id)
		self.assertEqual("+1000 to Attack Rating", result2.formatted)

		result3 = decodeProp(stream)
		self.assertIsNone(result3)

	def test_decode_prop_none_pattern(self):
		ostream = OBitStream()
		ostream.append(81, 9)
		ostream.append(0, 7)

		stream = IBitStream(bytearray(ostream.getByteList()))
		result = decodeProp(stream)

		self.assertIsNotNone(result)
		self.assertEqual(81, result.id)
		self.assertEqual("Knockback", result.formatted)
