import unittest
import os

from lib import Charm
from lib import OBitStream
from . import FILE_ROOT_DIR

DIR=os.path.join(FILE_ROOT_DIR, 'charm')

class TestCharm(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()


	def test_charm_of_greed(self):
		item = Charm("cm1 ", 0x115) # of greed
		item.setGfx(1)

		item.addProp(79); # +411%(9 bits) extra gold from monsters
		item.addProp(80); # +155%(8 bits) Better Chance of Getting Magic Items
		item.addProp(127); # +7 (3 bits) to All Skill Level
		item.addProp(239); # (6 bits) Extra Gold from Monsters (Based on Character Level)
		item.addProp(240); # (6 bits) Better Chance of Getting Magic Items (Based on Character Level)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 80 00 65", self.s.toHexString()[:7*3-1])

		with open(os.path.join(DIR, "of_greed.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_charm_of_skill(self):
		item = Charm("cm1 ", 0x0f1) # of Skill

		item.addProp(85); # +x% exp gain
		item.addProp(127); # +7 (3 bits) to All Skill Level

		# non-class skill (97), Valkyrie (32), level (+FF)
		item.addProp(97, 32, 0xFF)
		# non-class skill (97), Teleport (54), level (+FF)
		item.addProp(97, 54, 0xFF)

		# aura when equipped (151), Conviction (123), level (+31)
		item.addProp(151, 123, 0xFF)

		# cast level X "Lower Resist(91)" chance Y on striking
		item.addProp(198, 0xffff, 91, 0xffff)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 80 00 65", self.s.toHexString()[:7*3-1])

		with open(os.path.join(DIR, "of_skill_aura_conviction.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_charm_of_slaying(self):
		item = Charm("cm1 ", 0x026)

		# max resist
		item.addProp(38)
		item.addProp(40)
		item.addProp(42)
		item.addProp(44)
		item.addProp(46)

		item.addProp(333) # Enenmy resistance Cold
		item.addProp(334)
		item.addProp(335)
		item.addProp(336)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 80 00 65", self.s.toHexString()[:7*3-1])

		with open(os.path.join(DIR, "of_slaying.d2i"), "wb") as f:
			self.s.writeBytes(f)
