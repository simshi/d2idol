import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import HighQualityItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_pole_of_soul_harvest():
	s = OBitStream()
	item = HighQualityItem("7s8 ", 4, 3)

	# 23: +1 to 2h Minimum Damage
	item.addProp(23)
	# 24: +1 to 2h Maximum Damage
	item.addProp(24)
	# 60: 1% Life stolen per hit
	item.addProp(60)
	# 93: 1% Faster Hit Recovery
	item.addProp(93)
	# 135: 1% Chance of Crushing Blow
	item.addProp(135)
	# 136: 1% Chance of Open Wounds
	item.addProp(136)
	# 198: cast Hydra (level 53, 100% Chance) on striking
	item.addProp(198, 0xffff, 53, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[HighQuality]pole_of_soulharvest.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_phase_blade_5():
	s = OBitStream()
	item = HighQualityItem("7cr ", 5, 3)

	# 17: +1% Enhanced Damage
	item.addProp(17)
	# 19: +1 to Attack Rating
	item.addProp(19)
	# 52: Adds 1-1 magic damage
	item.addProp(52)
	# 53: Adds 1 magic damage
	item.addProp(53)
	# 218: +1 to Defense (Based on Character Level)
	item.addProp(218)
	# 219: 1% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 60: 1% Life stolen per hit
	item.addProp(60)
	# 62: 1% Mana stolen per hit
	item.addProp(62)
	# 119: +1 to Monster Defense Per Hit
	item.addProp(119)
	# 135: 1% Chance of Crushing Blow
	item.addProp(135)
	# 136: 1% Chance of Open Wounds
	item.addProp(136)
	# 195: cast Amplify Damage (level 87, 100% Chance) on attack
	item.addProp(195, 0xffff, 87, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[HighQuality]phase_blade_5.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sacred_rondache_4():
	s = OBitStream()
	item = HighQualityItem("pac ", 4, 3)

	item.addPropGroup("basicdefense")
	# 20: 1% Increased Chance of Blocking
	item.addProp(20)
	# 39: Fire Resist +1%
	item.addProp(39)
	# 41: Lightning Resist +1%
	item.addProp(41)
	# 43: Cold Resist +1%
	item.addProp(43)
	# 45: Poison Resist +1%
	item.addProp(45)

	item.writeStream(s)

	with open(os.path.join(DIR, "[HighQuality]sacred_rondache_4.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_archon_plate_3():
	s = OBitStream()
	item = HighQualityItem("utp ", 3, 3)

	# 214: +1 to Defense (Based on Character Level)
	item.addProp(214)
	# 215: 1% Enhanced Defense (Based on Character Level)
	item.addProp(215)
	# 3: +1 to Vitality
	item.addProp(3)
	
	# +All Resist (Fire, Lightning, Cold, Poison)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)

	# 198: cast Hydra (level 104, 100% Chance) on striking
	item.addProp(198, 0xffff, 104, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "superior/archon_plate_3.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_archon_plate_4():
	s = OBitStream()
	item = HighQualityItem("utp ", 4, 3)

	# 214: +1 to Defense (Based on Character Level)
	item.addProp(214)
	# 215: 1% Enhanced Defense (Based on Character Level)
	item.addProp(215)
	# 3: +1 to Vitality
	item.addProp(3)
	# 198: cast Hydra (level 104, 100% Chance) on striking
	item.addProp(198, 0xffff, 104, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "superior/archon_plate_4.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_pole_of_soul_harvest()
	generate_phase_blade_5()
	generate_sacred_rondache_4()
	generate_archon_plate_3()
	generate_archon_plate_4()
	print("High Quality items generated successfully!")
