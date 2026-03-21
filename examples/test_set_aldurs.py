import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_aldurs_helm_stony_gaze():
	s = OBitStream()
	item = SetItem("dr8 ", 0x42)

	# 16: +1% Enhanced Defense
	item.addProp(16)
	# 31: +1 Defense
	item.addProp(31)
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
	# 1: +1 to Strength
	item.addSetProp(1, 1)
	# 1: +1 to Energy
	item.addSetProp(2, 1)
	# 222: +1 to Vitality (Based on Character Level)
	item.addSetProp(3, 222)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_armor_deception():
	s = OBitStream()
	item = SetItem("uul ", 0x43)

	item.addPropGroup("basicdefense")
	# 201: cast Weaken (level 92, 100% Chance) when struck
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	# 151: Add Aura (Level 102) When Equipped
	item.addProp(151, 102, 0xFF)
	# 188: +40 to Elemental Skills (Druid Only)
	item.addProp(188, 40, 0xff)
	# 3: +3 to Vitality
	item.addSetProp(1, 3)
	# 3: +3 to Dexterity
	item.addSetProp(2, 3)
	# 223: +1 to Dexterity (Based on Character Level)
	item.addSetProp(3, 223)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_weapon_rhythm():
	s = OBitStream()
	item = SetItem("9mt ", 0x44)
	# 91: Requirements -0%
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	# 21: +1 to Minimum Damage
	item.addProp(21)
	# 22: +1 to Maximum Damage
	item.addProp(22)
	# 198: cast Hydra (level 53, 100% Chance) on striking
	item.addProp(198, 0xffff, 53, 0xffff)
	# 0: +1 to Strength
	item.addSetProp(1, 0)
	# 0: +1 to Energy
	item.addSetProp(2, 0)
	# 220: +1 to Strength (Based on Character Level)
	item.addSetProp(3, 220)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_weapon.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_boots_advance():
	s = OBitStream()
	item = SetItem("xtb ", 0x45)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	# 2: +1 to Dexterity
	item.addSetProp(1, 2)
	# 2: +1 to Vitality
	item.addSetProp(2, 2)
	# 221: +1 to Energy (Based on Character Level)
	item.addSetProp(3, 221)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_boots.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_aldurs_helm_stony_gaze()
	generate_aldurs_armor_deception()
	generate_aldurs_weapon_rhythm()
	generate_aldurs_boots_advance()
	print("Aldur's Watchtower set items generated successfully!")
