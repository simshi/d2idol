import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_aldurs_helm_stony_gaze():
	s = OBitStream()
	item = SetItem("dr8 ", 0x42)

	item.addProp(16)
	item.addProp(31)
	item.addProp(99)
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 42, 0xffff)
	item.addProp(330)
	item.addProp(329)
	item.addSetProp(1, 1)
	item.addSetProp(2, 1)
	item.addSetProp(3, 222)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_armor_deception():
	s = OBitStream()
	item = SetItem("uul ", 0x43)

	item.addPropGroup("basicdefense")
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	item.addProp(151, 102, 0xFF)
	item.addProp(188, 40, 0xff)
	item.addSetProp(1, 3)
	item.addSetProp(2, 3)
	item.addSetProp(3, 223)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_weapon_rhythm():
	s = OBitStream()
	item = SetItem("9mt ", 0x44)
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	item.addProp(21)
	item.addProp(22)
	item.addProp(198, 0xffff, 53, 0xffff)
	item.addSetProp(1, 0)
	item.addSetProp(2, 0)
	item.addSetProp(3, 220)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]aldurs_weapon.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_aldurs_boots_advance():
	s = OBitStream()
	item = SetItem("xtb ", 0x45)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	item.addSetProp(1, 2)
	item.addSetProp(2, 2)
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
