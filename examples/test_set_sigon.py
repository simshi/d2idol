import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_sigon_glove():
	s = OBitStream()
	item = SetItem("hgl ", 0x23)

	item.addPropGroup("mf")
	# 19: +1 to Attack Rating
	item.addProp(19)
	# 119: +1 to Monster Defense Per Hit
	item.addProp(119)
	# 150: Slows Target by 1%
	item.addProp(150)
	# 93: 1% Better Chance of Getting Magic Items (Based on Character Level)
	item.addSetProp(0, 93)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_gage.glove.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_helm():
	s = OBitStream()
	item = SetItem("ghm ", 0x24)

	item.addPropGroup("mf")
	# 151: Add Aura (Level 118) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast Hydra (level 42, 100% Chance) on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 126: +2 to Combat Skills (Barbarian Only)
	item.addProp(126, 2, 0xff)
	# 224: +1 to Attack Rating (Based on Character Level)
	item.addSetProp(0, 224)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_visor.helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_armor():
	s = OBitStream()
	item = SetItem("gth ", 0x25)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	# 238: +1% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 238)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_shelter.armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_belt():
	s = OBitStream()
	item = SetItem("hbl ", 0x27)

	item.addPropGroup("mf")
	# 234: +1 to Poison Damage Over 1 Seconds
	item.addProp(234)
	# 235: +1 to Minimum Poison Damage
	item.addProp(235)
	# 236: +1 to Maximum Poison Damage
	item.addProp(236)
	# 237: +1 to Poison Damage
	item.addProp(237)
	# 151: Add Aura (Level 125) When Equipped
	item.addProp(151, 125, 0xFF)
	# 214: +1 to Defense (Based on Character Level)
	item.addSetProp(0, 214)
	# 215: 1% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 215)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_wrap.belt.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_shield():
	s = OBitStream()
	item = SetItem("tow ", 0x28)

	item.addPropGroup("mf")
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

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_guard.shield.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_sigon_glove()
	generate_sigon_helm()
	generate_sigon_armor()
	generate_sigon_belt()
	generate_sigon_shield()
	print("Sigon's Complete Steel set items generated successfully!")
