import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import UniqItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_amulet_of_rixots_keen():
	s = OBitStream()
	item = UniqItem("amu ", 25)

	item.addPropGroup("characteristic")
	item.addPropGroup("mf")
	item.addPropGroup("defense")

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]amulet_of_rixots_keen.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_ring_nagelring():
	s = OBitStream()
	item = UniqItem("rin ", 0x78)

	item.addProp(127)
	item.addPropGroup("mf")
	item.addPropGroup("greed")
	item.addProp(127)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]ring_of_nagelring.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_torso_of_greyform():
	s = OBitStream()
	item = UniqItem("qui ", 79)

	item.addPropGroup("characteristic")
	item.addPropGroup("mf")
	item.addPropGroup("defense")
	item.addProp(201, 0xFFFF, 92, 0xFFFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]greyform.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_pole_of_soul_harvest():
	s = OBitStream()
	item = UniqItem("scy ", 0x32)

	item.addProp(91, 0)
	item.addProp(23)
	item.addProp(24)
	item.addPropGroup("offense")
	item.addProp(151, 120, 0xFF)
	item.addProp(198, 0xffff, 56, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]pole_of_soulharvest.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_bow_of_kuko_shakaku():
	s = OBitStream()
	item = UniqItem("8lb ", 0xbe)

	item.addProp(91, 0)
	item.addProp(23)
	item.addProp(24)
	item.addPropGroup("offense")
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 56, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]bow_of_kKukoShakaku.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_bow_of_pluckeye():
	s = OBitStream()
	item = UniqItem("sbb ", 0x3b)

	item.addProp(91, 0)
	item.addProp(23)
	item.addProp(24)
	item.addPropGroup("offense")
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 56, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]bow_of_pluckeye.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_javelin_of_pluckeye():
	s = OBitStream()
	item = UniqItem("tsp ", 25)

	item.addProp(91, 0)
	item.addProp(23)
	item.addProp(24)
	item.addPropGroup("offense")
	item.addProp(159)
	item.addProp(160)
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 53, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]javelin.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_claw_of_pluckeye():
	s = OBitStream()
	item = UniqItem("skr ", 25)
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	item.addProp(21)
	item.addProp(22)
	item.addProp(218)
	item.addProp(219)
	item.addProp(198, 0xffff, 53, 0xffff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Uniq]claw.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_amulet_of_rixots_keen()
	generate_ring_nagelring()
	generate_torso_of_greyform()
	generate_pole_of_soul_harvest()
	generate_bow_of_kuko_shakaku()
	generate_bow_of_pluckeye()
	generate_javelin_of_pluckeye()
	generate_claw_of_pluckeye()
	print("Unique items generated successfully!")
