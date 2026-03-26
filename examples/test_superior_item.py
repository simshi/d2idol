import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from lib import OBitStream
from lib import HighQualityItem


DIR = os.path.join("..", "output", "superior")


def generate_archon_plate_3():
    s = OBitStream()
    item = HighQualityItem("utp ", 3, 3)

    # 214: +63 Defense (Based on Character Level)
    item.addProp(214)
    # 215: +63% Enhanced Defense (Based on Character Level)
    item.addProp(215)
    # 3: +223 to Dexterity
    item.addProp(3)

    item.addPropGroup("allresist")

    # 151: Add Defiance Aura (Level 31) When Equipped
    item.addProp(151, 104, 0xFF)

    item.writeStream(s)

    with open(os.path.join(DIR, "archon_plate_3.d2i"), "wb") as f:
        s.writeBytes(f)


def generate_archon_plate_4():
    s = OBitStream()
    item = HighQualityItem("utp ", 4, 3)

    # 214: +63 Defense (Based on Character Level)
    item.addProp(214)
    # 215: +63% Enhanced Defense (Based on Character Level)
    item.addProp(215)
    # 3: +223 to Dexterity
    item.addProp(3)

    # 151: Add Defiance Aura (Level 31) When Equipped
    item.addProp(151, 104, 0xFF)

    item.writeStream(s)

    with open(os.path.join(DIR, "archon_plate_4.d2i"), "wb") as f:
        s.writeBytes(f)


if __name__ == "__main__":
    generate_archon_plate_3()
    generate_archon_plate_4()
    print("Superior items generated successfully!")
