import os

from lib import Charm
from lib import OBitStream

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT_DIR, "output", "charm")


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
    # 97: Skill Valkyrie (id=32) +255
    item.addProp(97, 32, 0xFF)
    # 97: Skill Teleport (id=54) +255
    item.addProp(97, 54, 0xFF)
    # 151: Add Conviction Aura (Level 31) When Equipped
    item.addProp(151, 123, 0xFF)
    # 198: cast level 63 Lower Resist 127% Chance on striking
    item.addProp(198, 0xFFFF, 91, 0xFFFF)

    item.writeStream(s)

    with open(os.path.join(DIR, "of_skill_aura_conviction.d2i"), "wb") as f:
        s.writeBytes(f)


def generate_charm_of_shock():
    s = OBitStream()
    item = Charm("cm1 ", 0x0BD)

    item.addProp(151, 118)  # Holy Shock
    item.addProp(144) # +127% Lightning Absorb
    item.addProp(330) # +x Lightning damage
    # 334: -255% to Enemy Lightning Resistance
    item.addProp(334)

    item.writeStream(s)

    with open(os.path.join(DIR, "of_shock.d2i"), "wb") as f:
        s.writeBytes(f)


def generate_charm_of_frost():
    s = OBitStream()
    item = Charm("cm1 ", 0x2b6)

    item.addProp(151, 114)  # Holy Freeze
    item.addProp(148) # +127% Cold Absorb
    item.addProp(331) # +x Cold damage
    # 335: -255% to Enemy Cold Resistance
    item.addProp(335)

    item.writeStream(s)

    with open(os.path.join(DIR, "of_frost.d2i"), "wb") as f:
        s.writeBytes(f)


def generate_charm_of_the_sun():
    s = OBitStream()
    item = Charm("cm1 ", 0x138)

    item.addProp(151, 102)  # Holy Fire
    item.addProp(142) # +127% Fire Absorb
    item.addProp(329) # +x fire damage
    # 333: -255% to Enemy Fire Resistance
    item.addProp(333)

    item.writeStream(s)

    with open(os.path.join(DIR, "of_the_sun.d2i"), "wb") as f:
        s.writeBytes(f)


def generate_charm_of_the_brilliance():
    s = OBitStream()
    item = Charm("cm1 ", 0x12d)

    item.addProp(151, 119)  # Sanctuary
    item.addProp(52) # +255-512 Magic Damage
    item.addProp(53) # +512 Magic Damage
    item.addProp(146) # +127% Magic Absorb

    item.writeStream(s)

    with open(os.path.join(DIR, "of_brilliance.d2i"), "wb") as f:
        s.writeBytes(f)


def generate_charm_of_slaying():
    s = OBitStream()
    item = Charm("cm1 ", 0x026)

    # 38: +31%% to Maximum Magic Resist
    item.addProp(38)
    # 40: +31%% to Maximum Fire Resist
    item.addProp(40)
    # 42: +31%% to Maximum Lightning Resist
    item.addProp(42)
    # 44: +31%% to Maximum Cold Resist
    item.addProp(44)
    # 46: +31%% to Maximum Poison Resist
    item.addProp(46)
    # 116: -127%% Target Defense
    item.addProp(116)
    # 333: -255%% to Enemy Cold Resistance
    item.addProp(333)
    # 334: -255%% to Enemy Fire Resistance
    item.addProp(334)
    # 335: -255%% to Enemy Lightning Resistance
    item.addProp(335)
    # 336: -255%% to Enemy Poison Resistance
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
    generate_charm_of_shock()
    generate_charm_of_frost()
    generate_charm_of_the_sun()
    generate_charm_of_the_brilliance()
    generate_charm_of_slaying()
    generate_charm_of_apprentice()
    print("Charm items generated successfully!")
