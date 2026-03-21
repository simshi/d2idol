import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_griswolds_redemption_scep():
	s = OBitStream()
	item = SetItem("7ws ", 0x53)
	# 91: Requirements -100%
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	# 21: +63 to Minimum Damage
	item.addProp(21)
	# 22: +127 to Maximum Damage
	item.addProp(22)
	# 218: +63 Defense (Based on Character Level)
	item.addProp(218)
	# 219: +63% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 135: 127% Chance of Crushing Blow
	item.addProp(135)
	# 136: 127% Chance of Open Wounds
	item.addProp(136)
	# 120: -128 to Monster Defense Per Hit
	item.addProp(120, 0)

	# 151: Add Fanaticism Aura (Level 31) When Equipped
	item.addProp(151, 122, 0xFF)
	# 198: cast level 63 Frozen Orb 127% Chance on striking
	item.addProp(198, 0xffff, 64, 0xffff)
	# + Set 0: Skill Set Combat (Paladin) +7
	item.addSetProp(0, 188, 24, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_redemption_scep.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_valor_helm():
	s = OBitStream()
	item = SetItem("urn ", 0x51)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 198: cast level 63 Static Field 127% Chance on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# + Set 0: Skill Set Offensive Auras (Paladin) +7
	item.addSetProp(0, 188, 25, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_valor_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_heart_plate():
	s = OBitStream()
	item = SetItem("xar ", 0x52)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	item.addPropGroup("allresist")

	# 201: cast level 63 Poison Nova 127% Chance when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)

	# 188: Skill Set Defensive Auras (Paladin) +7
	item.addProp(188, 26, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_heart_plate.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_honor_shield():
	s = OBitStream()
	item = SetItem("paf ", 0x54)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 20: 63% Increased Chance of Blocking
	item.addProp(20)
	# 102: 107% Faster Block Rate
	item.addProp(102)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_honor_shield.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_tooth_sword():
	s = OBitStream()
	item = SetItem("lsd ", 0x6)
	# 91: Requirements -100%
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	# 21: +63 to Minimum Damage
	item.addProp(21)
	# 22: +127 to Maximum Damage
	item.addProp(22)
	# 151: Add Holy Fire Aura (Level 31) When Equipped
	item.addProp(151, 102, 0xFF)
	# 198: cast level 63 Chain Lightning 127% Chance on striking
	item.addProp(198, 0xffff, 53, 0xffff)
	# + Set 0: +63 Defense (Based on Character Level)
	item.addSetProp(0, 218)
	# + Set 0: +63% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 219)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_tooth_swor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_claw_shield():
	s = OBitStream()
	item = SetItem("sml ", 0x7)

	# 16: +511% Enhanced Defense
	item.addProp(16)
	# 31: +2057 Defense
	item.addProp(31)
	# 214: +63 Defense (Based on Character Level)
	item.addProp(214)
	# 215: +63% Enhanced Defense (Based on Character Level)
	item.addProp(215)
	# 78: Attacker Takes Damage of 127
	item.addProp(78)
	# 81: Knockback
	item.addProp(81)
	# 102: 107% Faster Block Rate
	item.addProp(102)
	# + Set 0: Add Thorns Aura (Level 31) When Equipped
	item.addSetProp(0, 151, 103, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_claw_shield.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_pincers_glove():
	s = OBitStream()
	item = SetItem("mgl ", 0x8)

	item.addPropGroup("mf")
	# 19: +511%-511% Enhanced Damage
	item.addProp(19)
	# 119: +491% to Attack Rating
	item.addProp(119)
	# 150: Slows Target by 127%
	item.addProp(150)
	# + Set 0: +63 Defense (Based on Character Level)
	item.addSetProp(0, 218)
	# + Set 0: +63% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 219)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_pincers_glove.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_leather():
	s = OBitStream()
	item = SetItem("stu ", 0x76)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	item.addPropGroup("allresist")

	# 201: cast level 63 Poison Nova 127% Chance when struck
	item.addProp(201, 0xFFFF, 92, 0xffff)
	# 126: +7 to Poison Skills
	item.addProp(126, 3, 0xff)
	# 151: Add Holy Fire Aura (Level 31) When Equipped
	item.addProp(151, 102, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_leather.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_hat():
	s = OBitStream()
	item = SetItem("xap ", 0x75)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Holy Shock Aura (Level 31) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast level 63 Static Field 127% Chance on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 126: +7 to Lightning Skills
	item.addProp(126, 2, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_hat.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_boots():
	s = OBitStream()
	item = SetItem("vbt ", 0x77)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Vigor Aura (Level 31) When Equipped
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_boots.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_helm():
	s = OBitStream()
	item = SetItem("xh9 ", 0x3e)

	# 35: Damage Reduced by 63
	item.addProp(35)
	# 151: Add Holy Shock Aura (Level 31) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast level 63 Static Field 127% Chance on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 330: +461% to Lightning Skill Damage
	item.addProp(330)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_scissors():
	s = OBitStream()
	item = SetItem("7qr ", 0x3f)

	item.addPropGroup("basicoffense")
	# 21: +63 to Minimum Damage
	item.addProp(21)
	# 22: +127 to Maximum Damage
	item.addProp(22)
	# 218: +63 Defense (Based on Character Level)
	item.addProp(218)
	# 219: +63% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 198: cast level 63 Chain Lightning 127% Chance on striking
	item.addProp(198, 0xffff, 53, 0xffff)
	# 330: +461% to Lightning Skill Damage
	item.addProp(330)
	# 188: Skill Set Martial Arts +7
	item.addProp(188, 50, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_scissors.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_armor():
	s = OBitStream()
	item = SetItem("ucl ", 0x40)

	item.addPropGroup("basicdefense")
	item.addPropGroup("allresist")

	# 201: cast level 63 Poison Nova 127% Chance when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	# 151: Add Holy Fire Aura (Level 31) When Equipped
	item.addProp(151, 102, 0xFF)
	# 329: +461% to Fire Skill Damage
	item.addProp(329)
	# 332: +461% to Poison Skill Damage
	item.addProp(332)
	# 188: Skill Set Shadow Disciplines +7
	item.addProp(188, 49, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_boots():
	s = OBitStream()
	item = SetItem("xmb ", 0x41)

	# 67: 97% Faster Run/Walk
	item.addProp(67)
	# 137: +127 Kick Damage
	item.addProp(137)
	# 249: +63 Kick Damage (Based on Character Level)
	item.addProp(249)
	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Vigor Aura (Level 31) When Equipped
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_boots.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_helm():
	s = OBitStream()
	item = SetItem("uh9 ", 0x55)

	# 78: Attacker Takes Damage of 127
	item.addProp(78)
	# 99: 107% Faster Hit Recovery
	item.addProp(99)
	# 151: Add Holy Shock Aura (Level 31) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast level 63 Static Field 127% Chance on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 330: +461% to Lightning Skill Damage
	item.addProp(330)
	# 329: +461% to Fire Skill Damage
	item.addProp(329)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_armor():
	s = OBitStream()
	item = SetItem("xul ", 0x56)

	item.addPropGroup("basicdefense")
	# 201: cast level 63 Poison Nova 127% Chance when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	# 151: Add Holy Fire Aura (Level 31) When Equipped
	item.addProp(151, 102, 0xFF)
	# + Set 1: +205% Fire Resist
	item.addSetProp(1, 39)
	# + Set 1: +205% Lightning Resist
	item.addSetProp(1, 41)
	# + Set 1: +205% Cold Resist
	item.addSetProp(1, 43)
	# + Set 1: +205% Poison Resist
	item.addSetProp(1, 45)
	# + Set 3: Damage Reduced by 255%
	item.addSetProp(3, 36)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_trophy():
	s = OBitStream()
	item = SetItem("ne9 ", 0x57)

	# 20: 63% Increased Chance of Blocking
	item.addProp(20)
	# 102: 107% Faster Block Rate
	item.addProp(102)
	# 188: Skill Set Poison and Bone (Necromancer) +7
	item.addProp(188, 17, 0xff)
	# + Set 1: +63% Damage to Undead (Based on Character Level)
	item.addSetProp(1, 336)
	# + Set 2: Add Thorns Aura (Level 31) When Equipped
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
	# 332: +461% to Poison Skill Damage
	item.addProp(332)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_gloves.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_belt():
	s = OBitStream()
	item = SetItem("utc ", 0x59)

	# 7: +479 to Life
	item.addProp(7)
	# 9: +223 to Mana
	item.addProp(9)
	# 11: +223 to Maximum Stamina
	item.addProp(11)
	# 74: Replenish Life +33
	item.addProp(74)
	# 76: Increase Maximum Life 53%
	item.addProp(76)
	# 77: Increase Maximum Mana 53%
	item.addProp(77)
	# + Set 1: Cannot Be Frozen
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
