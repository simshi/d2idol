import os

from lib import SetItem
from lib import OBitStream

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT_DIR, "output", "set")


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

	with open(os.path.join(DIR, "griswolds_redemption_scep.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "griswolds_valor_helm.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "griswolds_heart_plate.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "griswolds_honor_shield.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "cleglaws_tooth_swor.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "cleglaws_claw_shield.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "cleglaws_pincers_glove.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "cowkings_leather.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "cowkings_hat.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_boots():
	s = OBitStream()
	item = SetItem("vbt ", 0x77)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 151: Add Vigor Aura (Level 31) When Equipped
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "cowkings_boots.d2i"), "wb") as f:
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
	print("Set items generated successfully!")
