import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output", "set")


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

	with open(os.path.join(DIR, "trangouls_helm.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "trangouls_armor.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "trangouls_trophy.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "trangouls_gloves.d2i"), "wb") as f:
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

	with open(os.path.join(DIR, "trangouls_belt.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_trangouls_helm()
	generate_trangouls_armor()
	generate_trangouls_trophy()
	generate_trangouls_gloves()
	generate_trangouls_belt()
	print("Trangoul's set items generated successfully!")
