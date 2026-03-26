import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output", "set")


def generate_sigon_glove():
	s = OBitStream()
	item = SetItem("hgl ", 0x23)

	item.addPropGroup("mf")
	# 19: +511%-511% Enhanced Damage
	item.addProp(19)
	# 119: +491% to Attack Rating
	item.addProp(119)
	# 150: Slows Target by 127%
	item.addProp(150)
	# + Set 0: +155% Better Chance of Getting Magic Items
	item.addSetProp(0, 93)

	item.writeStream(s)

	with open(os.path.join(DIR, "sigon_gage.glove.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_helm():
	s = OBitStream()
	item = SetItem("ghm ", 0x24)

	item.addPropGroup("mf")
	# 151: Add Holy Shock Aura (Level 31) When Equipped
	item.addProp(151, 118, 0xFF)
	# 198: cast level 63 Static Field 127% Chance on striking
	item.addProp(198, 0xffff, 42, 0xffff)
	# 126: +7 to Lightning Skills
	item.addProp(126, 2, 0xff)
	# + Set 0: +63 Attack Rating (Based on Character Level)
	item.addSetProp(0, 224)

	item.writeStream(s)

	with open(os.path.join(DIR, "sigon_visor.helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_armor():
	s = OBitStream()
	item = SetItem("gth ", 0x25)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	# + Set 0: +63% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 238)

	item.writeStream(s)

	with open(os.path.join(DIR, "sigon_shelter.armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_belt():
	s = OBitStream()
	item = SetItem("hbl ", 0x27)

	item.addPropGroup("mf")
	# 234: +63% Cold Absorb (Based on Character Level)
	item.addProp(234)
	# 235: +63% Fire Absorb (Based on Character Level)
	item.addProp(235)
	# 236: +63% Lightning Absorb (Based on Character Level)
	item.addProp(236)
	# 237: +63% Poison Absorb (Based on Character Level)
	item.addProp(237)
	# 151: Add Salvation Aura (Level 31) When Equipped
	item.addProp(151, 125, 0xFF)
	# + Set 0: +63 Defense (Based on Character Level)
	item.addSetProp(0, 214)
	# + Set 0: +63% Enhanced Defense (Based on Character Level)
	item.addSetProp(0, 215)

	item.writeStream(s)

	with open(os.path.join(DIR, "sigon_wrap.belt.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_shield():
	s = OBitStream()
	item = SetItem("tow ", 0x28)

	item.addPropGroup("mf")
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

	item.writeStream(s)

	with open(os.path.join(DIR, "sigon_guard.shield.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_sigon_glove()
	generate_sigon_helm()
	generate_sigon_armor()
	generate_sigon_belt()
	generate_sigon_shield()
	print("Sigon's Complete Steel set items generated successfully!")
