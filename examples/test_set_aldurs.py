import os

from lib import SetItem
from lib import OBitStream

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT_DIR, "output", "set")


def generate_aldurs_helm_stony_gaze():
	s = OBitStream()
	item = SetItem("dr8 ", 0x42)

	# 16: +511% Enhanced Defense
	item.addProp(16)
	# 31: +2057 Defense
	item.addProp(31)
	# 99: 107% Faster Hit Recovery
	item.addProp(99)
	# 151: Add Holy Shock Aura (Level 31) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast level 63 Static Field 127% Chance on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 329: +461% to Fire Skill Damage
	item.addProp(329)
	# 330: +461% to Lightning Skill Damage
	item.addProp(330)

	# + Set 1: +223 Strength
	item.addSetProp(1, 0)
	# + Set 2: +95 Energy
	item.addSetProp(2, 1)
	# + Set 3: +63 Vitality (Based on Character Level)
	item.addSetProp(3, 222)

	item.writeStream(s)

	with open(os.path.join(DIR, "aldurs_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_armor_deception():
	s = OBitStream()
	item = SetItem("uul ", 0x43)

	item.addPropGroup("basicdefense")
	# 201: cast level 63 Poison Nova 127% Chance when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	# 151: Add Holy Fire Aura (Level 31) When Equipped
	item.addProp(151, 102, 0xFF)
	# 188: Skill Set Summoning (Druid) +7
	item.addProp(188, 40, 0xff)
	# + Set 2: +95 Dexterity
	item.addSetProp(2, 2)
	# + Set 1: +95 Vitality
	item.addSetProp(1, 3)
	# + Set 3: +63 Dexterity (Based on Character Level)
	item.addSetProp(3, 223)

	item.writeStream(s)

	with open(os.path.join(DIR, "aldurs_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_weapon_rhythm():
	s = OBitStream()
	item = SetItem("9mt ", 0x44)
	# 91: Requirements -100%
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	# 21: +63 to Minimum Damage
	item.addProp(21)
	# 22: +127 to Maximum Damage
	item.addProp(22)
	# 198: cast level 63 Chain Lightning 127% Chance on striking
	item.addProp(198, 0xffff, 53, 0xffff)
	# + Set 1: +223 Strength
	item.addSetProp(1, 0)
	# + Set 2: +95 Energy
	item.addSetProp(2, 1)
	# + Set 3: +63 Strength (Based on Character Level)
	item.addSetProp(3, 220)

	item.writeStream(s)

	with open(os.path.join(DIR, "aldurs_weapon.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_boots_advance():
	s = OBitStream()
	item = SetItem("xtb ", 0x45)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# + Set 1: +95 Dexterity
	item.addSetProp(1, 2)
	# + Set 2: +95 Vitality
	item.addSetProp(2, 3)
	# + Set 3: +63 Energy (Based on Character Level)
	item.addSetProp(3, 221)

	item.writeStream(s)

	with open(os.path.join(DIR, "aldurs_boots.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_aldurs_helm_stony_gaze()
	generate_aldurs_armor_deception()
	generate_aldurs_weapon_rhythm()
	generate_aldurs_boots_advance()
	print("Aldur's Watchtower set items generated successfully!")
