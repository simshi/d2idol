#!/usr/bin/env python3

import sys
from lib import quality, IBitStream
from lib.character_class import CharacterClass
from lib.itemprops import decodeProp
from lib.itemtype import iTypeFromCode


def decodeProps(stream: IBitStream):
    nProps = 0
    while not stream.isEnd():
        result = decodeProp(stream)
        if result is None:
            break
        nProps += 1
        print("[{0:4d}]".format(result.id), "{0}".format(
            result.formatted) if result.formatted else "")
        for detail in result.details:
            if detail.base and detail.base > 0:
                print("\t{0}({1})={2}-{3}".format(detail.ptn,
                      detail.bits, detail.value, detail.base))
            else:
                print("\t{0}({1})={2}{3}".format(
                    detail.ptn, detail.bits, detail.value,
                    " ({0})".format(detail.name) if detail.name else ""))
    print("nProps={0}".format(nProps))


def parseEar(stream: IBitStream):
    iClass = stream.read(3)
    iLevel = stream.read(7)
    print("iClass={0}({1}),iLvl={2}".format(
        CharacterClass.from_id(iClass), iClass, iLevel))
    name = ""
    while True:
        c = stream.read(7)
        if c == 0:
            break
        name += chr(c)
    print("name={0}".format(name))


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

    version = stream.read(10)
    print("version={0}({1})".format(
        "expansion" if version == 0x64 else "<unknown>", version))

    stream.skip(18)
    print("[{0:5d}:] base done".format(stream.getOffset()))

    if bEar:
        parseEar(stream)
        return

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
