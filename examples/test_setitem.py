import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib import SetItem
from lib import OBitStream

DIR = os.path.join("..", "output")


def generate_griswolds_redemption_scep():
	s = OBitStream()
	item = SetItem("7ws ", 0x53)
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	item.addProp(21)
	item.addProp(22)
	item.addProp(218)
	item.addProp(219)
	item.addProp(135)
	item.addProp(136)
	item.addProp(120, 0)

	item.addProp(151, 122, 0xFF)
	item.addProp(198, 0xffff, 64, 0xffff)
	item.addSetProp(0, 188, 24, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_redemption_scep.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_valor_helm():
	s = OBitStream()
	item = SetItem("urn ", 0x51)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	item.addProp(198, 0xffff, 42, 0xffff)
	item.addSetProp(0, 188, 25, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_valor_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_heart_plate():
	s = OBitStream()
	item = SetItem("xar ", 0x52)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)
	item.addProp(188, 26, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_heart_plate.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_griswolds_honor_shield():
	s = OBitStream()
	item = SetItem("paf ", 0x54)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	item.addProp(20)
	item.addProp(102)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]griswolds_honor_shield.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_tooth_sword():
	s = OBitStream()
	item = SetItem("lsd ", 0x6)
	item.addProp(91, 0)

	item.addPropGroup("basicoffense")
	item.addProp(21)
	item.addProp(22)
	item.addProp(151, 102, 0xFF)
	item.addProp(198, 0xffff, 53, 0xffff)
	item.addSetProp(0, 218)
	item.addSetProp(0, 219)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_tooth_swor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_claw_shield():
	s = OBitStream()
	item = SetItem("sml ", 0x7)

	item.addProp(16)
	item.addProp(31)
	item.addProp(214)
	item.addProp(215)
	item.addProp(78)
	item.addProp(81)
	item.addProp(102)
	item.addSetProp(0, 151, 103, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_claw_shield.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cleglaws_pincers_glove():
	s = OBitStream()
	item = SetItem("mgl ", 0x8)

	item.addPropGroup("mf")
	item.addProp(19)
	item.addProp(119)
	item.addProp(150)
	item.addSetProp(0, 218)
	item.addSetProp(0, 219)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cleglaws_pincers_glove.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_leather():
	s = OBitStream()
	item = SetItem("stu ", 0x76)

	item.addPropGroup("characteristic")
	item.addPropGroup("basicdefense")
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	item.addProp(126, 3, 0xff)
	item.addProp(151, 102, 0xFF)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_leather.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_hat():
	s = OBitStream()
	item = SetItem("xap ", 0x75)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 42, 0xffff)
	item.addProp(126, 2, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_hat.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_cowkings_boots():
	s = OBitStream()
	item = SetItem("vbt ", 0x77)

	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]cowkings_boots.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_helm():
	s = OBitStream()
	item = SetItem("xh9 ", 0x3e)

	item.addProp(35)
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 42, 0xffff)
	item.addProp(330)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_scissors():
	s = OBitStream()
	item = SetItem("7qr ", 0x3f)

	item.addPropGroup("basicoffense")
	item.addProp(21)
	item.addProp(22)
	item.addProp(218)
	item.addProp(219)
	item.addProp(198, 0xffff, 53, 0xffff)
	item.addProp(330)
	item.addProp(188, 50, 0xff)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_scissors.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_armor():
	s = OBitStream()
	item = SetItem("ucl ", 0x40)

	item.addPropGroup("basicdefense")
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	item.addProp(151, 102, 0xFF)
	item.addProp(329)
	item.addProp(332)
	item.addProp(188, 49, 0xff)
	item.addProp(39)
	item.addProp(41)
	item.addProp(43)
	item.addProp(45)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_natalya_boots():
	s = OBitStream()
	item = SetItem("xmb ", 0x41)

	item.addProp(67)
	item.addProp(137)
	item.addProp(249)
	item.addPropGroup("basicdefense")
	item.addPropGroup("mf")
	item.addProp(151, 115, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]natalya_boots.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_helm():
	s = OBitStream()
	item = SetItem("uh9 ", 0x55)

	item.addProp(78)
	item.addProp(99)
	item.addProp(151, 118, 0xFF)
	item.addProp(198, 0xffff, 42, 0xffff)
	item.addProp(330)
	item.addProp(329)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_helm.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_armor():
	s = OBitStream()
	item = SetItem("xul ", 0x56)

	item.addPropGroup("basicdefense")
	item.addProp(201, 0xFFFF, 92, 0xFFFF)
	item.addProp(151, 102, 0xFF)
	item.addSetProp(1, 39)
	item.addSetProp(1, 41)
	item.addSetProp(1, 43)
	item.addSetProp(1, 45)
	item.addSetProp(3, 36)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_armor.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_trophy():
	s = OBitStream()
	item = SetItem("ne9 ", 0x57)

	item.addProp(20)
	item.addProp(102)
	item.addProp(188, 17, 0xff)
	item.addSetProp(1, 336)
	item.addSetProp(2, 151, 103, 0xFF)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_trophy.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_gloves():
	s = OBitStream()
	item = SetItem("xmg ", 0x58)

	item.addPropGroup("mf")
	item.addProp(105)
	item.addProp(229)
	item.addProp(332)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_gloves.d2i"), "wb") as f:
		s.writeBytes(f)


def generate_trangouls_belt():
	s = OBitStream()
	item = SetItem("utc ", 0x59)

	item.addProp(7)
	item.addProp(9)
	item.addProp(11)
	item.addProp(74)
	item.addProp(76)
	item.addProp(77)
	item.addSetProp(1, 153)

	item.writeStream(s)

	with open(os.path.join(DIR, "[Set]trangouls_belt.d2i"), "wb") as f:
		s.writeBytes(f)


if __name__ == "__main__":
	generate_griswolds_redemption_scep()
	generate_griswolds_valor_helm()
	generate_griswolds_heart_plate()
	generate_griswolds_honor_shield()
	generate_cleglaws_tooth_sword()
	generate_cleglaws_claw_shield()
	generate_cleglaws_pincers_glove()
	generate_cowkings_leather()
	generate_cowkings_hat()
	generate_cowkings_boots()
	generate_natalya_helm()
	generate_natalya_scissors()
	generate_natalya_armor()
	generate_natalya_boots()
	generate_trangouls_helm()
	generate_trangouls_armor()
	generate_trangouls_trophy()
	generate_trangouls_gloves()
	generate_trangouls_belt()
	print("Set items generated successfully!")
