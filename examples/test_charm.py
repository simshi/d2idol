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

	item.addProp(79)
	item.addProp(80)
	item.addProp(127)
	item.addProp(239)
	item.addProp(240)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_greed.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_charm_of_skill():
	s = OBitStream()
	item = Charm("cm1 ", 0x0F1)

	item.addProp(85)
	item.addProp(127)
	item.addProp(97, 32, 0xFF)
	item.addProp(97, 54, 0xFF)
	item.addProp(151, 123, 0xFF)
	item.addProp(198, 0xFFFF, 91, 0xFFFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_skill_aura_conviction.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_charm_of_slaying():
	s = OBitStream()
	item = Charm("cm1 ", 0x026)

	item.addProp(38)
	item.addProp(40)
	item.addProp(42)
	item.addProp(44)
	item.addProp(46)
	item.addProp(116)
	item.addProp(333)
	item.addProp(334)
	item.addProp(335)
	item.addProp(336)

	item.writeStream(s)

	with open(os.path.join(DIR, "of_slaying.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_charm_of_apprentice():
	s = OBitStream()
	item = Charm("cm1 ", 0x0AE)

	item.addProp(218)
	item.addProp(219)
	item.addProp(224)
	item.addProp(216)
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
