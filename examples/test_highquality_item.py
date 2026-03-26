import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import HighQualityItem
from lib import OBitStream

DIR = os.path.join("..", "output", "highquality")


def generate_pole_of_soul_harvest():
	s = OBitStream()
	item = HighQualityItem("7s8 ", 4, 3)

	# 23: +63 to 2h Minimum Damage
	item.addProp(23)
	# 24: +127 to 2h Maximum Damage
	item.addProp(24)
	# 60: 127% Life stolen per hit
	item.addProp(60)
	# 93: 107% Increased Attack Speed
	item.addProp(93)
	# 135: 127% Chance of Crushing Blow
	item.addProp(135)
	# 136: 127% Chance of Open Wounds
	item.addProp(136)
	# 198: cast level 63 Chain Lightning 127% Chance on striking
	item.addProp(198, 0xffff, 53, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "pole_of_soulharvest.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_phase_blade_5():
	s = OBitStream()
	item = HighQualityItem("7cr ", 5, 3)

	# 17: +1% Enhanced Damage
	item.addProp(17)
	# 19: +511%-511% Enhanced Damage
	item.addProp(19)
	# 52: Adds 255-511 magic damage
	item.addProp(52)
	# 53: Adds 511 magic damage
	item.addProp(53)
	# 218: +63 Defense (Based on Character Level)
	item.addProp(218)
	# 219: +63% Enhanced Defense (Based on Character Level)
	item.addProp(219)
	# 60: 127% Life stolen per hit
	item.addProp(60)
	# 62: 127% Mana stolen per hit
	item.addProp(62)
	# 119: +491% to Attack Rating
	item.addProp(119)
	# 135: 127% Chance of Crushing Blow
	item.addProp(135)
	# 136: 127% Chance of Open Wounds
	item.addProp(136)
	# 195: cast level 63 Decrepify 127% Chance on attack
	item.addProp(195, 0xffff, 87, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "phase_blade_5.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sacred_rondache_4():
	s = OBitStream()
	item = HighQualityItem("pac ", 4, 3)

	item.addPropGroup("basicdefense")
	# 20: 63% Increased Chance of Blocking
	item.addProp(20)

	item.addPropGroup("allresist")

	item.writeStream(s)

	with open(os.path.join(DIR, "sacred_rondache_4.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_pole_of_soul_harvest()
	generate_phase_blade_5()
	generate_sacred_rondache_4()
	print("High Quality items generated successfully!")
