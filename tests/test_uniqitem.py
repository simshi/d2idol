import unittest
import os

from lib import UniqItem
from lib import OBitStream
from . import FILE_ROOT_DIR


class TestUniqItem(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()


	def test_amu_of_rixots_keen(self):
		item = UniqItem("amu ", 25) # Rixot's

		# item.addProp(91)
		item.addPropGroup("characteristic")
		item.addPropGroup("mf")
		item.addPropGroup("defense")

		item.writeStream(self.s)
		result = str(self.s)
		self.assertEquals("1", result[20])
		self.assertEquals("4a 4d 10 00 80 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]amulet_of_rixots_keen.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_ring_nagelring(self):
		item = UniqItem("rin ", 0x78) # Nagelring

		item.addPropGroup("mf")
		item.addProp(127); # +7 (3 bits) to All Skill Level

		item.writeStream(self.s)
		self.assertEquals("4a 4d 10 00 80 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]ring_of_nagelring.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_tors_of_blinkbats_form(self):
		item = UniqItem("lea ", 80)

		item.addPropGroup("characteristic")
		item.addPropGroup("mf")
		item.addPropGroup("defense")

		# cast level X "Poison Nova(92)" chance Y on struck"
		item.addProp(201, 0xFFFF, 92, 0xFFFF)

		item.writeStream(self.s)
		self.assertEquals("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]tors_of_blinkbats_form.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_pole_of_soul_harvest(self):
		# SourHarvest in game is "scy ", not sure "hal " would always work!!!
		item = UniqItem("hal ", 0x32)

		item.addProp(91, 0); # requirment 0-100%
		item.addProp(23); # +(6bits) min 2 hands dmg
		item.addProp(24); # +(7bits) max 2 hands dmg
		item.addPropGroup("offense")

		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)

		# cast level X "Meteor(56)" chance Y on striking"
		item.addProp(198, 0xffff, 56, 0xffff)

		item.writeStream(self.s)
		self.assertEquals("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]pole_of_soulharvest.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_bow_of_KukoShakaku(self):
		item = UniqItem("8lb ", 0xbe)

		item.addProp(91, 0); # requirment 0-100%
		item.addProp(23); # +(6bits) min 2 hands dmg
		item.addProp(24); # +(7bits) max 2 hands dmg
		item.addPropGroup("offense")

		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)

		# cast level X "Meteor(56)" chance Y on striking"
		item.addProp(198, 0xffff, 56, 0xffff)

		item.writeStream(self.s)
		self.assertEquals("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]bow_of_kKukoShakaku.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_bow_of_Pluckeye(self):
		# "sbb " => Stormstrike(0x3f), reqLvl=23
		# "sbw " => Pluckeys(0x3b), reqLvl=7
		item = UniqItem("sbb ", 0x3b) # "sbw " => "sbb "

		item.addProp(91, 0); # requirment 0-100%
		item.addProp(23); # +(6bits) min 2 hands dmg
		item.addProp(24); # +(7bits) max 2 hands dmg
		item.addPropGroup("offense")

		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)

		# cast level X "Meteor(56)" chance Y on striking"
		item.addProp(198, 0xffff, 56, 0xffff)

		item.writeStream(self.s)
		self.assertEquals("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]bow_of_pluckeye.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_javelin_of_Pluckeye(self):
		item = UniqItem("tsp ", 25)

		item.addProp(91, 0); # requirment 0-100%
		item.addProp(23); # +(6bits) min 2 hands dmg
		item.addProp(24); # +(7bits) max 2 hands dmg
		item.addPropGroup("offense")
		item.addProp(159) # +d to min Throw Damage
		item.addProp(160) # +d to max Throw Damage

		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)

		# cast level X "Chain Lightning(53)" chance Y on striking"
		item.addProp(198, 0xffff, 53, 0xffff)

		item.writeStream(self.s)
		self.assertEquals("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[UniqItem]javelin.d2i"), "wb") as f:
			self.s.writeBytes(f)