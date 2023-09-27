import unittest
import os

from lib import SetItem
from lib import OBitStream
from . import FILE_ROOT_DIR


class TestSetSigon(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()

	def test_glove(self):
		item = SetItem("hgl ", 0x23)

		item.addPropGroup("mf")
		item.addProp(19) #+d to Attack Rating
		item.addProp(119) #+x% to Attack Rating
		item.addProp(150) # Slows Target by x%

		item.addSetProp(0, 93) #+%d to Attack Speed

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[Set]sigon_gage.glove.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_helm(self):
		item = SetItem("ghm ", 0x24)

		# item.addPropGroup("basicdefense")
		item.addPropGroup("mf")

		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)
		# cast level X "Static Field (42)" chance Y on striking"
		item.addProp(198, 0xffff, 42, 0xffff)
		item.addProp(126, 2, 0xff) # Lightning(2) Skills +x

		item.addSetProp(0, 224) #+d attack rating per level

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[Set]sigon_visor.helm.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_armor(self):
		item = SetItem("gth ", 0x25)

		item.addPropGroup("characteristic")
		item.addPropGroup("basicdefense")
		# item.addPropGroup("mf")

		item.addSetProp(0, 238) #+d damage taken by attacker

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[Set]sigon_shelter.armor.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_belt(self):
		item = SetItem("hbl ", 0x27)

		item.addPropGroup("basicdefense")
		item.addProp(234) # +%d cold absorb (level)
		item.addProp(235) # +%d fire absorb (level)
		item.addProp(236) # +%d lightning absorb (level)
		item.addProp(237) # +%d poison absorb (level)

		item.addSetProp(0, 214) #+%d to Defense (Based on Character Level)
		item.addSetProp(0, 215) #+%d%% to Defense (Based on Character Level)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[Set]sigon_wrap.belt.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_shield(self):
		item = SetItem("tow ", 0x28)

		item.addPropGroup("mf")
		# item.addPropGroup("basicdefense")
		item.addProp(16)
		item.addProp(31)
		item.addProp(214)
		item.addProp(215)

		item.addProp(78) #Attacker Takes Damage of %d
		item.addProp(81) #Knockback
		item.addProp(102) #+d% Faster Block Rate

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[Set]sigon_guard.shield.d2i"), "wb") as f:
			self.s.writeBytes(f)
