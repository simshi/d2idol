#!/usr/bin/env python3

import sys
from lib import quality, IBitStream
from lib.itemprops import getPropFromID
from lib.itemtype import iTypeFromCode
import lib.itemprops as itemprops


def decodeProps(stream):
    nProps = 0
    while not stream.isEnd():
        id = stream.read(9)
        if id == 0x1ff:
            break
        nProps += 1
        prop = getPropFromID(id)
        print("id:{0},{1}".format(id, prop))
        params = []
        base_value = prop[1]
        i = 0
        for n in prop[0]:
            if n == 0:
                break
            v = stream.read(n)

            if base_value > 0:
                v -= base_value

            ptn = prop[3][i]
            if ptn == itemprops.ptnRaw:
                params.append(v)
                print("\traw({1})={0}".format(v, n))
            elif ptn == itemprops.ptnSkill:
                skill_name = itemprops.getSkillName(v)
                params.append(skill_name)
                print("\tskill({1})={0} ({2})".format(v, n, skill_name))
            elif ptn == itemprops.ptnSkillTree:
                tree_name = itemprops.getSkillTreeName(v)
                params.append(tree_name)
                print("\tskillTree({1})={0} ({2})".format(v, n, tree_name))
            elif ptn == itemprops.ptnClass:
                params.append(v)
                print("\tclass({1})={0}".format(v, n))
            elif ptn == itemprops.ptnDuration:
                params.append(v)
                print("\tduration({1})={0}".format(v, n))
            elif ptn == itemprops.ptnTime:
                params.append(v)
                print("\ttime({1})={0}".format(v, n))
            i += 1

        try:
            if params:
                formatted = prop[2].format(*params)
                print("\tformatted: {0}".format(formatted))
        except Exception as e:
            print("\tformat error: {0}".format(e))
    print("nProps={0}".format(nProps))


def parseD2I(data):
    stream = IBitStream(data)
    print(str(stream))
    pad = 0
    for v in str(stream)[-7:]:
        if v == '0':
            pad += 1
    print("pad={0}/{1}".format(pad, len(stream)), str(stream)[-7:])

    d = 0x4d4a
    s = 16
    v = ('{0:032b}'.format(d))[::-1][:s]
    print("searching :{0}-{1},{2}".format(d, s, v))
    for i in range(0, len(stream)):
        if str(stream)[i:i+s] == v:
            bits = int(str(stream)[i:i+s][::-1], 2)
            print("\t", i, bits)

    stream.skip(2*8+1+3)
    bIdentified = stream.read(1)
    stream.skip(27 - stream.getOffset())
    bSocketed = stream.read(1)
    print("bIdentified={0},bSocketed={1}".format(bIdentified, bSocketed))
    stream.skip(2 + 1 + 1)
    bEar = stream.read(1)
    stream.skip(1 + 3)
    bSimple = stream.read(1)
    bEthereal = stream.read(1)
    print("bEar={0},bSimple={1},bEthereal={2}".format(
        bEar, bSimple, bEthereal))
    print("offset:", stream.getOffset())
    stream.skip(1)  # unk47

    bPersonalized = stream.read(1)

    stream.skip(1)  # unk51
    bRuneWord = stream.read(1)
    print("bPersonalized={0},bRune={1}".format(bPersonalized, bRuneWord))
    stream.skip(5)

    stream.skip(76 - stream.getOffset())
    code = stream.readString(4)
    nGems = stream.read(3)
    print("code={0},#gems={1}".format(code, nGems))

    guid = stream.read(32)
    iLevel = stream.read(7)
    print("guid=0x{0:04x},iLvl={1}".format(guid, iLevel))

    iQuality = stream.read(4)
    print("iQuality={0}-{1}".format(iQuality, quality.byId[iQuality]))

    bVarGfx = stream.read(1)
    if bVarGfx:
        iVarGfx = stream.read(3)
        print("iVarGfx={0}".format(iVarGfx))

    bClass = stream.read(1)
    if bClass:
        wClass = stream.read(11)
        print("wClass={0}".format(wClass))

    if iQuality == quality.High:
        iQualitySubType = stream.read(3)
        print("\tsubType={0}(0x{0:x})".format(iQualitySubType))
    elif iQuality == quality.Magic:
        prefix = stream.read(11)
        assert prefix == 0, "Magic's prefix must be 0"
        suffix = stream.read(11)
        print("\tMagic: suffix={0}(0x{0:x})".format(suffix))
    elif iQuality == quality.Unique:
        iUniqId = stream.read(12)
        print("\tUniqItem: id={0}(0x{0:x})".format(iUniqId))
    elif iQuality == quality.PartOfSet:
        iSetId = stream.read(12)
        print("\tSetItem: id={0}(0x{0:x})".format(iSetId))
    else:
        print("\t?", iQuality)

    if bRuneWord:
        wRuneWord = stream.read(16)
        stream.skip(7 - 16)
        print("runeWord:", wRuneWord, "offset:", stream.getOffset())

    bTimestamp = stream.read(1)
    if bTimestamp:
        dw3 = stream.read(32*3)
        print("dwTimestamp?=0x{0:x}".format(dw3))

    bits = "{0:08b}".format(stream.peek(8))
    print("offset before type data", stream.getOffset(), bits[::-1])
    sType, typeCfg = iTypeFromCode(code)
    print("type: {0} - {1}".format(sType, typeCfg["name"]))
    if sType == "weapon":
        print("type specific:", str(stream)[
              stream.getOffset():stream.getOffset()+17], stream.getOffset())
        if typeCfg["nodurability"]:
            d = stream.read(8)
            stream.skip(9)
            print("\tdurability: INDESTRUCTIBLE(pad=0x{0:x})".format(d))
        else:
            max_durability = stream.read(8)
            if max_durability > 0:
                durability = stream.read(9)
                print(
                    "\tdurability: {0}/{1}".format(durability, max_durability))
            else:
                print("\tdurability: INDESTRUCTIBLE")

        if typeCfg["maxstack"] > 0:
            print("\tquantity:", stream.read(9))

    elif sType == "armor":
        iDefence = stream.read(11)
        print("\tiDefence={0}".format(iDefence))

        iMaxDur = stream.read(8)
        if iMaxDur > 0:
            iCurDur = stream.read(9)
            print("\tdurability={0}/{1}".format(iCurDur, iMaxDur))
        else:
            print("\tIndestructible")

    if bSocketed:
        iSockets = stream.read(4)
        print("\tsockets: {0}".format(iSockets))

    bits = "{0:09b}".format(stream.peek(9))
    print("offset before props data", stream.getOffset(), bits[::-1])
    if bRuneWord:
        print(">>>> props from white:")
        decodeProps(stream)
        print(">>>> props from Rune Word:")

    decodeProps(stream)

    if stream.getOffset()+pad != len(stream):
        print("offset:{0}+{1}/{2}".format(stream.getOffset(), pad, len(stream)))
    else:
        print("offset:{0}".format(stream.getOffset()))


if __name__ == "__main__":
    from pathlib import Path
    import re
    raw = sys.argv[1]

    # Git-Bash/MSYS 风格 /d/...  ->  D:/...
    win = re.sub(r'^/([a-zA-Z])/', r'\1:/', raw)
    path = Path(win).resolve()
    print('映射后路径:', path)
    print('exists:', path.exists())

    with path.open('rb') as f:
        parseD2I(f.read())
