import unittest
import os

from lib import SetItem
from lib import OBitStream
from . import FILE_ROOT_DIR


class TestSetItem(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()


	def test_GriswoldsRedemption_scep(self):
		item = SetItem("7ws ", 0x53)
		item.addProp(91, 0); # requirment 0-100%

		item.addPropGroup("basicoffense")
		item.addProp(21); # +(6bits) min 1 hand dmg
		item.addProp(22); # +(7bits) max 1 hand dmg
		item.addProp(218) #+%d to Maximum Damage (Based on Character Level)
		item.addProp(219) #%d%% Enhanced Maximum Damage (Based on Character Level)
		item.addProp(135) #%d%% Chance of Open Wounds
		item.addProp(136) #%d%% Chance of Crushing Blow
		item.addProp(120, 0) #%d(-128) to Monster Defense Per Hit

		# aura when equipped (151), Fanaticism (122), level (+31)
		item.addProp(151, 122, 0xFF)

		# cast level X "Frozen Orb(64)" chance Y on striking"
		item.addProp(198, 0xffff, 64, 0xffff)


		item.addSetProp(0, 188, 24, 0xff) #Skills set X (24-PAL/Combat) +%d
		# item.addSetProp(0, 218) #+%d to Maximum Damage (Based on Character Level)
		# item.addSetProp(0, 219) #%d%% Enhanced Maximum Damage (Based on Character Level)

		# item.addSetProp(1, 218) #+%d to Maximum Damage (Based on Character Level)
		# item.addSetProp(1, 219) #%d%% Enhanced Maximum Damage (Based on Character Level)

		# item.addSetProp(2, 218) #+%d to Maximum Damage (Based on Character Level)
		# item.addSetProp(2, 219) #%d%% Enhanced Maximum Damage (Based on Character Level)

		item.writeStream(self.s)
		b = self.s.getByteList()
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]griswolds_redemption_scep.d2i"), "wb") as f:
			self.s.writeBytes(f)


	def test_GriswoldsValor_helm(self):
		item = SetItem("urn ", 0x51)

		item.addPropGroup("basicdefense")
		item.addPropGroup("mf")

		# cast level X "Static Field (42)" chance Y on striking"
		item.addProp(198, 0xffff, 42, 0xffff)


		item.addSetProp(0, 188, 25, 0xff) #Skills set X (25-PAL/OffensiveAura) +%d
		# item.addSetProp(1, 214) #+%d to Defense (Based on Character Level)
		# item.addSetProp(1, 215) #%d%% Enhanced Defense (Based on Character Level)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]griswolds_valor_helm.d2i"), "wb") as f:
			self.s.writeBytes(f)


	def test_GriswoldsHeart_plate(self):
		item = SetItem("xar ", 0x52)

		item.addPropGroup("characteristic")
		item.addPropGroup("basicdefense")
		# item.addPropGroup("mf")
		# cast level X "Poison Nova(92)" chance Y on struck"
		item.addProp(201, 0xFFFF, 92, 0xFFFF)

		item.addProp(39)
		item.addProp(41)
		item.addProp(43)
		item.addProp(45)
		item.addProp(188, 26, 0xff) #Skills set X (25-PAL/DefensiveAura) +%d

		# whether there were set props depends on game config!!!
		# item.addSetProp(0, 188, 26, 0xff) #Skills set X (25-PAL/DefensiveAura) +%d
		# item.addSetProp(0, 214) #+%d to Defense (Based on Character Level)
		# item.addSetProp(0, 215) #%d%% Enhanced Defense (Based on Character Level)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]griswolds_heart_plate.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_GriswoldsHonor_shield(self):
		item = SetItem("paf ", 0x54)

		item.addPropGroup("basicdefense")
		item.addPropGroup("mf")
		item.addProp(20) #+x% Increased Chance of Blocking
		item.addProp(102) #+x% Faster Block Rate


		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]griswolds_honor_shield.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_CleglawsTooth_sword(self):
		item = SetItem("lsd ", 0x6)
		item.addProp(91, 0); # requirment 0-100%

		item.addPropGroup("basicoffense")
		item.addProp(21); # +(6bits) min 1 hand dmg
		item.addProp(22); # +(7bits) max 1 hand dmg

		# # aura when equipped (151), Fanaticism (122), level (+31)
		# item.addProp(151, 122, 0xFF)
		# aura when equipped (151), Holy Fire(102), level (+31)
		item.addProp(151, 102, 0xFF)

		# cast level X "Chain Lightning(53)" chance Y on striking"
		item.addProp(198, 0xffff, 53, 0xffff)


		item.addSetProp(0, 218) #+%d to Maximum Damage (Based on Character Level)
		item.addSetProp(0, 219) #%d%% Enhanced Maximum Damage (Based on Character Level)
		# item.addSetProp(0, 188, 24, 0xff) #Skills set X (24-PAL/Combat) +%d

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]cleglaws_tooth_swor.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_CleglawsClaw_shield(self):
		item = SetItem("sml ", 0x7)

		# item.addPropGroup("basicdefense")
		item.addProp(16)
		item.addProp(31)
		item.addProp(214)
		item.addProp(215)

		item.addProp(78) #Attacker Takes Damage of %d
		item.addProp(81) #Knockback
		item.addProp(102) #+d% Faster Block Rate


		# aura when equipped (151), Thorns (103), level (+31)
		item.addSetProp(0, 151, 103, 0xFF)
		# item.addSetProp(0, 188, 26, 0xff) #Skills set X (26-PAL/DefensiveAura) +%d

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]cleglaws_claw_shield.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_CleglawsPincers_glove(self):
		item = SetItem("mgl ", 0x8)

		item.addPropGroup("mf")
		item.addProp(19) #+d to Attack Rating
		item.addProp(119) #+x% to Attack Rating
		item.addProp(150) # Slows Target by x%


		item.addSetProp(0, 218) #+%d to Maximum Damage (Based on Character Level)
		item.addSetProp(0, 219) #%d%% Enhanced Maximum Damage (Based on Character Level)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]cleglaws_pincers_glove.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_CowKings_leather(self):
		item = SetItem("stu ", 0x76)

		item.addPropGroup("characteristic")
		item.addPropGroup("basicdefense")
		# item.addPropGroup("mf")
		# cast level X "Poison Nova(92)" chance Y on struck"
		item.addProp(201, 0xFFFF, 92, 0xFFFF)
		item.addProp(126, 3, 0xff) # Poision(3) Skills +x
		# aura when equipped (151), Holy Fire(102), level (+31)
		item.addProp(151, 102, 0xFF)

		item.addProp(39)
		item.addProp(41)
		item.addProp(43)
		item.addProp(45)


		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]cowkings_leather.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_CowKings_hat(self):
		item = SetItem("xap ", 0x75)

		item.addPropGroup("basicdefense")
		item.addPropGroup("mf")

		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)
		# cast level X "Static Field (42)" chance Y on striking"
		item.addProp(198, 0xffff, 42, 0xffff)
		item.addProp(126, 2, 0xff) # Lightning(2) Skills +x

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]cowkings_hat.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_CowKings_boots(self):
		item = SetItem("vbt ", 0x77)

		item.addPropGroup("basicdefense")
		item.addPropGroup("mf")

		# aura when equipped (151), Vigor(115), level (+31)
		item.addProp(151, 115, 0xFF)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]cowkings_boots.d2i"), "wb") as f:
			self.s.writeBytes(f)

	# Assassin
	def test_Natalya_helm(self):
		item = SetItem("xh9 ", 0x3e)

		item.addProp(35) # Magic Damage Reduced by %d
		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)
		# cast level X "Static Field (42)" chance Y on striking"
		item.addProp(198, 0xffff, 42, 0xffff)
		item.addProp(330) # +%d to Lightning Skill Damage

		# set item prop slot MUST follow game setting strictly!!!


		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]natalya_helm.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_Natalya_scissors(self):
		item = SetItem("7qr ", 0x3f)

		item.addPropGroup("basicoffense")
		item.addProp(21); # +(6bits) min 1 hand dmg
		item.addProp(22); # +(7bits) max 1 hand dmg
		item.addProp(218) #+%d to Maximum Damage (Based on Character Level)
		item.addProp(219) #%d%% Enhanced Maximum Damage (Based on Character Level)

		# cast level X "Chain Lightning(53)" chance Y on striking"
		item.addProp(198, 0xffff, 53, 0xffff)
		item.addProp(330) # +%d to Lightning Skill Damage

		item.addProp(188, 50, 0xff) #Skills set X (24-ASS/MartialArt) +%d

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]natalya_scissors.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_Natalya_armor(self):
		item = SetItem("ucl ", 0x40)

		# item.addPropGroup("characteristic")
		item.addPropGroup("basicdefense")
		# item.addPropGroup("mf")
		# cast level X "Poison Nova(92)" chance Y on struck"
		item.addProp(201, 0xFFFF, 92, 0xFFFF)
		# aura when equipped (151), Holy Fire(102), level (+31)
		item.addProp(151, 102, 0xFF)
		item.addProp(329) # x% to Fire Skill Damage
		item.addProp(332) # +%d to Poison Skill Damage
		item.addProp(188, 49, 0xff) #Skills set X (49-ASS/ShadowDiscipline) +%d

		item.addProp(39)
		item.addProp(41)
		item.addProp(43)
		item.addProp(45)
		# set item prop slot MUST follow game setting strictly!!!

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]natalya_armor.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_Natalya_boots(self):
		item = SetItem("xmb ", 0x41)

		item.addProp(67) # Faster Run/Walk
		item.addProp(137) # Kick Damage
		item.addProp(249) # Kick Damage (Based on Character Level)
		item.addPropGroup("basicdefense")
		item.addPropGroup("mf")

		# aura when equipped (151), Vigor(115), level (+31)
		item.addProp(151, 115, 0xFF)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]natalya_boots.d2i"), "wb") as f:
			self.s.writeBytes(f)

	# Necromancer
	def test_TrangOuls_helm(self):
		item = SetItem("uh9 ", 0x55)

		item.addProp(78) # Attacker Takes Damage of %d
		item.addProp(99) # Faster Hit Recovery x%
		# aura when equipped (151), Holy Shock(118), level (+31)
		item.addProp(151, 118, 0xFF)
		# cast level X "Static Field (42)" chance Y on striking"
		item.addProp(198, 0xffff, 42, 0xffff)
		item.addProp(330) # +%d to Lightning Skill Damage
		item.addProp(329) # x% to Fire Skill Damage

		# set item prop slot MUST follow game setting strictly!!!


		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]trangouls_helm.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_TrangOuls_armor(self):
		item = SetItem("xul ", 0x56)

		# item.addPropGroup("characteristic")
		item.addPropGroup("basicdefense")
		# item.addPropGroup("mf")
		# cast level X "Poison Nova(92)" chance Y on struck"
		item.addProp(201, 0xFFFF, 92, 0xFFFF)
		# aura when equipped (151), Holy Fire(102), level (+31)
		item.addProp(151, 102, 0xFF)

		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 39)
		item.addSetProp(1, 41)
		item.addSetProp(1, 43)
		item.addSetProp(1, 45)

		item.addSetProp(3, 36) # Damage Reduced by x%

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]trangouls_armor.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_TrangOuls_trophy(self):
		item = SetItem("ne9 ", 0x57)

		item.addProp(20) # x% Increased Chance of Blocking
		item.addProp(102) # +d% Faster Block Rate
		item.addProp(188, 17, 0xff) #Skills set X (17-NEC/PosionAndBone) +%d


		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 336) # x% to Enemy Poison Resistance
		# aura when equipped (151), Thorns (103), level (+31)
		item.addSetProp(2, 151, 103, 0xFF)


		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]trangouls_trophy.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_TrangOuls_gloves(self):
		item = SetItem("xmg ", 0x58)

		item.addPropGroup("mf")
		item.addProp(105) # x% Faster Cast Rate
		item.addProp(229) # +%d Poison Damage (Based on Character Level)
		item.addProp(332) # +%d to Poison Skill Damage

		# set item prop slot MUST follow game setting strictly!!!

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]trangouls_gloves.d2i"), "wb") as f:
			self.s.writeBytes(f)

	def test_TrangOuls_belt(self):
		item = SetItem("utc ", 0x59)

		item.addProp(7) # +d Life
		item.addProp(9) # +d Mana
		item.addProp(11) # +d Maximum Stamina
		item.addProp(74) # Replenish Life +%d
		item.addProp(76) # x% Max Life
		item.addProp(77) # x% Max Mana
		# item.addPropGroup("mf")

		# set item prop slot MUST follow game setting strictly!!!
		item.addSetProp(1, 153) # Cannot Be Frozen


		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 00 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[SetItem]trangouls_belt.d2i"), "wb") as f:
			self.s.writeBytes(f)
