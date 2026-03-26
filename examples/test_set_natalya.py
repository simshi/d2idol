import os

from lib import SetItem
from lib import OBitStream

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT_DIR, "output", "set")


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

	with open(os.path.join(DIR, "natalya_helm.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "natalya_scissors.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "natalya_armor.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "natalya_boots.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_natalya_helm()
	generate_natalya_scissors()
	generate_natalya_armor()
	generate_natalya_boots()
	print("Natalya's set items generated successfully!")
