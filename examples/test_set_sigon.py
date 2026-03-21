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
	item.addProp(19)
	item.addProp(119)
	item.addProp(150)
	item.addSetProp(0, 93)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_gage.glove.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_helm():
	s = OBitStream()
	item = SetItem("ghm ", 0x24)

	item.addPropGroup("mf")
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 42, 0xffff)
	item.addProp(126, 2, 0xff)
	item.addSetProp(0, 224)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_visor.helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_armor():
	s = OBitStream()
	item = SetItem("gth ", 0x25)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	item.addSetProp(0, 238)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_shelter.armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_belt():
	s = OBitStream()
	item = SetItem("hbl ", 0x27)

	item.addPropGroup("mf")
	item.addProp(234)
	item.addProp(235)
	item.addProp(236)
	item.addProp(237)
	item.addProp(151, 125, 0xFF)
	item.addSetProp(0, 214)
	item.addSetProp(0, 215)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]sigon_wrap.belt.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_sigon_shield():
	s = OBitStream()
	item = SetItem("tow ", 0x28)

	item.addPropGroup("mf")
	item.addProp(16)
	item.addProp(31)
	item.addProp(214)
	item.addProp(215)
	item.addProp(78)
	item.addProp(81)
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
