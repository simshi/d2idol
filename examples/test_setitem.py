import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_griswolds_redemption_scep():
	s = OBitStream()
	item = SetItem("7ws ", 0x53)
	# 91: Requirements -0%
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	# 21: +1 to Minimum Damage
	item.addProp(21)
	# 22: +1 to Maximum Damage
	item.addProp(22)
	# 218: +1 to Defense (Based on Character Level)
	item.addProp(218)
	# 219: 1% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 135: 1% Chance of Crushing Blow
	item.addProp(135)
	# 136: 1% Chance of Open Wounds
	item.addProp(136)
	# 120: 0 to Monster Defense Per Hit
	item.addProp(120, 0)

	# 151: Add Aura (Level 122) When Equipped
	item.addProp(151, 122, 0xFF)
	# 198: cast Hydra (level 64, 100% Chance) on striking
	item.addProp(198, 0xffff, 64, 0xffff)
	# 188: +24 to Fire Skills (Sorceress Only)
	item.addSetProp(0, 188, 24, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_redemption_scep.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_valor_helm():
	s = OBitStream()
	item = SetItem("urn ", 0x51)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 198: cast Hydra (level 42, 100% Chance) on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 188: +25 to Fire Skills (Sorceress Only)
	item.addSetProp(0, 188, 25, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_valor_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_heart_plate():
	s = OBitStream()
	item = SetItem("xar ", 0x52)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	# 201: cast Weaken (level 92, 100% Chance) when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)

	# +All Resist (Fire, Lightning, Cold, Poison)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)

	# 188: +26 to Fire Skills (Sorceress Only)
	item.addProp(188, 26, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_heart_plate.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_honor_shield():
	s = OBitStream()
	item = SetItem("paf ", 0x54)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 20: 1% Increased Chance of Blocking
	item.addProp(20)
	# 102: 1% Faster Block Rate
	item.addProp(102)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_honor_shield.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_tooth_sword():
	s = OBitStream()
	item = SetItem("lsd ", 0x6)
	# 91: Requirements -0%
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	# 21: +1 to Minimum Damage
	item.addProp(21)
	# 22: +1 to Maximum Damage
	item.addProp(22)
	# 151: Add Aura (Level 102) When Equipped
	item.addProp(151, 102, 0xFF)
	# 198: cast Hydra (level 53, 100% Chance) on striking
	item.addProp(198, 0xffff, 53, 0xffff)
	# 218: +1 to Defense (Based on Character Level)
	item.addSetProp(0, 218)
	# 219: 1% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 219)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_tooth_swor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_claw_shield():
	s = OBitStream()
	item = SetItem("sml ", 0x7)

	# 16: +1% Enhanced Defense
	item.addProp(16)
	# 31: +1 Defense
	item.addProp(31)
	# 214: +1 to Defense (Based on Character Level)
	item.addProp(214)
	# 215: 1% Enhanced Defense (Based on Character Level)
	item.addProp(215)
	# 78: Replenish Life +1
	item.addProp(78)
	# 81: Knockback
	item.addProp(81)
	# 102: 1% Faster Block Rate
	item.addProp(102)
	# 151: Add Aura (Level 103) When Equipped
	item.addSetProp(0, 151, 103, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_claw_shield.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_pincers_glove():
	s = OBitStream()
	item = SetItem("mgl ", 0x8)

	item.addPropGroup("mf")
	# 19: +1 to Attack Rating
	item.addProp(19)
	# 119: +1 to Monster Defense Per Hit
	item.addProp(119)
	# 150: Slows Target by 1%
	item.addProp(150)
	# 218: +1 to Defense (Based on Character Level)
	item.addSetProp(0, 218)
	# 219: 1% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 219)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_pincers_glove.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_leather():
	s = OBitStream()
	item = SetItem("stu ", 0x76)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	# 201: cast Weaken (level 92, 100% Chance) when struck
	item.addProp(201, 0xFFFF, 92, 0xffff)
	# 126: +3 to Trap Skills (Assassin Only)
	item.addProp(126, 3, 0xff)
	# 151: Add Aura (Level 102) When Equipped
	item.addProp(151, 102, 0xFF)
	# 39: Fire Resist +1%
	item.addProp(39)
	# 41: Lightning Resist +1%
	item.addProp(41)
	# 43: Cold Resist +1%
	item.addProp(43)
	# 45: Poison Resist +1%
	item.addProp(45)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_leather.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_hat():
	s = OBitStream()
	item = SetItem("xap ", 0x75)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Aura (Level 118) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast Hydra (level 42, 100% Chance) on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 126: +2 to Trap Skills (Assassin Only)
	item.addProp(126, 2, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_hat.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_boots():
	s = OBitStream()
	item = SetItem("vbt ", 0x77)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Aura (Level 115) When Equipped
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_boots.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_helm():
	s = OBitStream()
	item = SetItem("xh9 ", 0x3e)

	# 35: Damage Reduced by 1
	item.addProp(35)
	# 151: Add Aura (Level 118) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast Hydra (level 42, 100% Chance) on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 330: Fire Resist +1% (Based on Character Level)
	item.addProp(330)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_scissors():
	s = OBitStream()
	item = SetItem("7qr ", 0x3f)

	item.addPropGroup("basicoffense")
	# 21: +1 to Minimum Damage
	item.addProp(21)
	# 22: +1 to Maximum Damage
	item.addProp(22)
	# 218: +1 to Defense (Based on Character Level)
	item.addProp(218)
	# 219: 1% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 198: cast Hydra (level 53, 100% Chance) on striking
	item.addProp(198, 0xffff, 53, 0xffff)
	# 330: Fire Resist +1% (Based on Character Level)
	item.addProp(330)
	# 188: +50 to Martial Arts (Assassin Only)
	item.addProp(188, 50, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_scissors.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_armor():
	s = OBitStream()
	item = SetItem("ucl ", 0x40)

	item.addPropGroup("basicdefense")
	# 201: cast Weaken (level 92, 100% Chance) when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	# 151: Add Aura (Level 102) When Equipped
	item.addProp(151, 102, 0xFF)
	# 329: Cold Resist +1% (Based on Character Level)
	item.addProp(329)
	# 332: Lightning Resist +1% (Based on Character Level)
	item.addProp(332)
	# 188: +49 to Shadow Disciplines (Assassin Only)
	item.addProp(188, 49, 0xff)
	# 39: Fire Resist +1%
	item.addProp(39)
	# 41: Lightning Resist +1%
	item.addProp(41)
	# 43: Cold Resist +1%
	item.addProp(43)
	# 45: Poison Resist +1%
	item.addProp(45)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_boots():
	s = OBitStream()
	item = SetItem("xmb ", 0x41)

	# 67: 1% Faster Run/Walk
	item.addProp(67)
	# 137: +1 to Mana After Each Kill
	item.addProp(137)
	# 249: 1% Chance of Deadly Strike (Based on Character Level)
	item.addProp(249)
	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Aura (Level 115) When Equipped
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_boots.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_helm():
	s = OBitStream()
	item = SetItem("uh9 ", 0x55)

	# 78: Replenish Life +1
	item.addProp(78)
	# 99: 1% Faster Hit Recovery
	item.addProp(99)
	# 151: Add Aura (Level 118) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast Hydra (level 42, 100% Chance) on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 330: Fire Resist +1% (Based on Character Level)
	item.addProp(330)
	# 329: Cold Resist +1% (Based on Character Level)
	item.addProp(329)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_armor():
	s = OBitStream()
	item = SetItem("xul ", 0x56)

	item.addPropGroup("basicdefense")
	# 201: cast Weaken (level 92, 100% Chance) when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	# 151: Add Aura (Level 102) When Equipped
	item.addProp(151, 102, 0xFF)
	# 39: Fire Resist +1%
	item.addSetProp(1, 39)
	# 41: Lightning Resist +1%
	item.addSetProp(1, 41)
	# 43: Cold Resist +1%
	item.addSetProp(1, 43)
	# 45: Poison Resist +1%
	item.addSetProp(1, 45)
	# 36: Damage Reduced by 1%
	item.addSetProp(3, 36)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_trophy():
	s = OBitStream()
	item = SetItem("ne9 ", 0x57)

	# 20: 1% Increased Chance of Blocking
	item.addProp(20)
	# 102: 1% Faster Block Rate
	item.addProp(102)
	# 188: +17 to Poison and Bone Skills (Necromancer Only)
	item.addProp(188, 17, 0xff)
	# 336: 1% Damage to Undead (Based on Character Level)
	item.addSetProp(1, 336)
	# 151: Add Aura (Level 103) When Equipped
	item.addSetProp(2, 151, 103, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_trophy.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_gloves():
	s = OBitStream()
	item = SetItem("xmg ", 0x58)

	item.addPropGroup("mf")
	# 105: 1% Faster Cast Rate
	item.addProp(105)
	# 229: Fire Resist +1% (Based on Character Level)
	item.addProp(229)
	# 332: Lightning Resist +1% (Based on Character Level)
	item.addProp(332)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_gloves.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_belt():
	s = OBitStream()
	item = SetItem("utc ", 0x59)

	# 7: +1 to Life
	item.addProp(7)
	# 9: +1 to Mana
	item.addProp(9)
	# 11: +1 to Maximum Stamina
	item.addProp(11)
	# 74: Replenish Life +1
	item.addProp(74)
	# 76: Increase Maximum Life 1%
	item.addProp(76)
	# 77: Increase Maximum Mana 1%
	item.addProp(77)
	# 153: Cannot Be Frozen
	item.addSetProp(1, 153)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_belt.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_griswolds_redemption_scep()
	generate_griswolds_valor_helm()
	generate_griswolds_heart_plate()
	generate_griswolds_honor_shield()
	generate_cleglaws_tooth_sword()
	generate_cleglaws_claw_shield()
	generate_cleglaws_pincers_glove()
	generate_cowkings_leather()
	generate_cowkings_hat()
	generate_cowkings_boots()
	generate_natalya_helm()
	generate_natalya_scissors()
	generate_natalya_armor()
	generate_natalya_boots()
	generate_trangouls_helm()
	generate_trangouls_armor()
	generate_trangouls_trophy()
	generate_trangouls_gloves()
	generate_trangouls_belt()
	print("Set items generated successfully!")
