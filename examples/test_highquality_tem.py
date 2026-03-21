import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import HighQualityItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_pole_of_soul_harvest():
	s = OBitStream()
	item = HighQualityItem("7s8 ", 4, 3)

	item.addProp(23)
	item.addProp(24)
	item.addProp(60)
	item.addProp(93)
	item.addProp(135)
	item.addProp(136)
	item.addProp(198, 0xffff, 53, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[HighQuality]pole_of_soulharvest.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_phase_blade_5():
	s = OBitStream()
	item = HighQualityItem("7cr ", 5, 3)

	item.addProp(17)
	item.addProp(19)
	item.addProp(52)
	item.addProp(53)
	item.addProp(218)
	item.addProp(219)
	item.addProp(60)
	item.addProp(62)
	item.addProp(119)
	item.addProp(135)
	item.addProp(136)
	item.addProp(195, 0xffff, 87, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[HighQuality]phase_blade_5.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sacred_rondache_4():
	s = OBitStream()
	item = HighQualityItem("pac ", 4, 3)

	item.addPropGroup("basicdefense")
	item.addProp(20)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)

	item.writeStream(s)

	with open(os.path.join(DIR, "[HighQuality]sacred_rondache_4.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_archon_plate_3():
	s = OBitStream()
	item = HighQualityItem("utp ", 3, 3)

	item.addProp(214)
	item.addProp(215)
	item.addProp(3)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)
	item.addProp(198, 0xffff, 104, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "superior/archon_plate_3.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_archon_plate_4():
	s = OBitStream()
	item = HighQualityItem("utp ", 4, 3)

	item.addProp(214)
	item.addProp(215)
	item.addProp(3)
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
