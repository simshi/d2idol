import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import Charm
from lib import OBitStream

DIR = os.path.join("..", "output", "charm")


def generate_charm_of_greed():
	s = OBitStream()
	item = Charm("cm1 ", 0x115)
	item.setGfx(1)

	# 79: Extra Gold from Monsters
	item.addProp(79)
	# 80: Better Chance of Getting Magic Items
	item.addProp(80)
	# 127: +X to All Skill Levels
	item.addProp(127)
	# 239: Extra Gold from Monsters (Based on Character Level)
	item.addProp(239)
	# 240: Better Chance of Getting Magic Items (Based on Character Level)
	item.addProp(240)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_greed.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_charm_of_skill():
	s = OBitStream()
	item = Charm("cm1 ", 0x0F1)

	# 85: +%d%% to Experience Gained
	item.addProp(85)
	# 127: +X to All Skill Levels
	item.addProp(127)
	# 97: Skill Valkyrie +63
	item.addProp(97, 32, 0xFF)
	# 97: Skill Teleport +63
	item.addProp(97, 54, 0xFF)
	# 151: Add Conviction Aura (Level 31) When Equipped
	item.addProp(151, 123, 0xFF)
	# 198: cast level 63 Lower Resist 127% Chance on striking
	item.addProp(198, 0xFFFF, 91, 0xFFFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_skill_aura_conviction.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_charm_of_slaying():
	s = OBitStream()
	item = Charm("cm1 ", 0x026)

	# 38: +%d%% to Maximum Fire Resist
	item.addProp(38)
	# 40: +%d%% to Maximum Lightning Resist
	item.addProp(40)
	# 42: +%d%% to Maximum Cold Resist
	item.addProp(42)
	# 44: +%d%% to Maximum Poison Resist
	item.addProp(44)
	# 46: +%d%% to Maximum Magic Resist
	item.addProp(46)
	# 116: +%d to Light Radius
	item.addProp(116)
	# 333: +%d%% to Attack Rating against Demons (Based on Character Level)
	item.addProp(333)
	# 334: +%d%% to Attack Rating against Undead (Based on Character Level)
	item.addProp(334)
	# 335: %d%% Damage to Demons (Based on Character Level)
	item.addProp(335)
	# 336: %d%% Damage to Undead (Based on Character Level)
	item.addProp(336)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_slaying.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_charm_of_apprentice():
	s = OBitStream()
	item = Charm("cm1 ", 0x0AE)

	# 218: +63 Defense (Based on Character Level)
	item.addProp(218)
	# 219: +63% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 224: +%d to Maximum Damage (Based on Character Level)
	item.addProp(224)
	# 216: +%d to Life (Based on Character Level)
	item.addProp(216)
	# 217: +%d to Mana (Based on Character Level)
	item.addProp(217)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_apprentice.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_charm_of_greed()
	generate_charm_of_skill()
	generate_charm_of_slaying()
	generate_charm_of_apprentice()
	print("Charm items generated successfully!")
