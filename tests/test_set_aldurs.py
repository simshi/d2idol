import unittest
import os

from lib import SetItem
from lib import OBitStream
from . import FILE_ROOT_DIR

# Druid
class TestSetAldursWatchtower(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()

	def test_helm_stony_gaze(self):
		item = SetItem("dr8 ", 0x42)

		item.addProp(16) # defense
		item.addProp(31) # defense
		item.addProp(99) # Faster Hit Recovery x%
		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)
		# cast level X "Static Field (42)" chance Y on striking"
		item.addProp(198, 0xffff, 42, 0xffff)
		item.addProp(330) # +%d to Lightning Skill Damage
		item.addProp(329) # x% to Fire Skill Damage

		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 1) # Energy
		item.addSetProp(2, 1) # Energy
		item.addSetProp(3, 222) # Energy +d/level

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]aldurs_helm.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_armor_deception(self):
		item = SetItem("uul ", 0x43)

		# item.addPropGroup("characteristic")
		item.addPropGroup("basicdefense")
		# item.addPropGroup("mf")
		# cast level X "Poison Nova(92)" chance Y on struck"
		item.addProp(201, 0xFFFF, 92, 0xFFFF)
		# aura when equipped (151), Holy Fire(102), level (+31)
		item.addProp(151, 102, 0xFF)

		item.addProp(188, 40, 0xff) # +d Druid Summoning(40) Skills

		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 3) # Vitality
		item.addSetProp(2, 3) # Vitality
		item.addSetProp(3, 223) # Vitality +d/level

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]aldurs_armor.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_weapon_rhythm(self):
		item = SetItem("9mt ", 0x44)
		item.addProp(91, 0); # requirment 0-100%

		item.addPropGroup("basicoffense")
		item.addProp(21); # +(6bits) min 1 hand dmg
		item.addProp(22); # +(7bits) max 1 hand dmg

		# cast level X "Chain Lightning(53)" chance Y on striking"
		item.addProp(198, 0xffff, 53, 0xffff)


		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 0) # Strength
		item.addSetProp(2, 0) #  Strength
		item.addSetProp(3, 220) # Strength +d/level

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]aldurs_weapon.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_boots_advance(self):
		item = SetItem("xtb ", 0x45)

		item.addPropGroup("basicdefense")
		item.addPropGroup("mf")

		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 2) # Dexteriy
		item.addSetProp(2, 2) # Dexteriy
		item.addSetProp(3, 221) # Dexteriy +d/level

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]aldurs_boots.d2i"), "wb") as f:
			self.s.writeBytes(f)# 	item.addProp(16) # defense
