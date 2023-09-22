import unittest
import os

from lib import HighQualityItem
from lib import OBitStream
from . import FILE_ROOT_DIR


class TestHighQualityItem(unittest.TestCase):
	def setUp(self):
		self.s = OBitStream()

	def test_pole_of_soul_harvest(self):
		item = HighQualityItem("7s8 ", 4, 3) # 精神Sprit 塔尔•书尔•欧特•安姆 Tal(7) + Thul(10) + Ort(9) + Amn(11)

		#item.addProp(91, 0) # requirment 0-100%
		item.addProp(23) # +(6bits) min 2 hands dmg
		item.addProp(24) # +(7bits) max 2 hands dmg
		item.addProp(93) # %d%% Increased Attack Speed
		#item.addPropGroup("offense")
		item.addProp(135) # #%d%% Chance of Open Wounds
		item.addProp(136) # %d%% Chance of Crushing Blow
		# item.addProp(17) # +%d-%d enhanced damage
		# item.addProp(75) # + max durability +d%

		# aura when equipped (151), Holy Shock(118), level (+31)
		#item.addProp(151, 118, 0xFF)

		# cast level X "Chain Lightning(53)" chance Y on striking"
		item.addProp(198, 0xffff, 53, 0xffff)

		item.writeStream(self.s)
		self.assertEqual("4a 4d 10 08 c0 00 64", self.s.toHexString()[:7*3-1])

		with open(os.path.join(FILE_ROOT_DIR, "[HighQualityItem]pole_of_soulharvest.d2i"), "wb") as f:
			self.s.writeBytes(f)