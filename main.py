#!/usr/bin/env python3

import sys
from lib import quality
from lib.itemprops import getPropFromID
from lib.itemtype import iTypeFromCode
import lib.itemprops as itemprops

# print("under construction, please use 'make test'")
def lebits2int(bits):
	return int(bits[::-1], 2)

def decodeProps(bits, offset):
	while offset < len(bits):
		id = lebits2int(bits[offset:offset+9])
		offset += 9
		if id == 0x1ff:
			break
		prop = getPropFromID(id)
		print("id:{0},{1}".format(id, prop))
		i = 0
		for n in prop[0]:
			if n == 0:
				break
			v = lebits2int(bits[offset:offset+n])
			offset += n

			ptn = prop[3][i]
			if ptn == itemprops.ptnRaw:
				print("\traw={0}".format(v))
			elif ptn == itemprops.ptnSkill:
				print("\tskill={0}".format(v))
			elif ptn == itemprops.ptnSkillTree:
				print("\tskillTree={0}".format(v))
			elif ptn == itemprops.ptnClass:
				print("\tclass={0}".format(v))
			elif ptn == itemprops.ptnDuration:
				print("\tduration={0}".format(v))
			elif ptn == itemprops.ptnTime:
				print("\ttime={0}".format(v))
			i += 1
	return offset

def parseD2I(bytes):
	bits = ''.join(["{0:08b}".format(v)[::-1] for v in bytes])
	print(bits)
	# TODO: if there are gems/runes followed, pad is at the end
	pad = 0
	for v in bits[-7:]:
		if v == '0':
			pad += 1
	print("pad={0}/{1}".format(pad, len(bits)), bits[-7:])

	# debug search
	d = 0x4d4a
	s = 16
	v = ('{0:032b}'.format(d))[::-1][:s]
	print("searching :{0}-{1},{2}".format(d, s, v))
	for i in range(0, len(bits)):
		if bits[i:i+s] == v:
			print("\t", i, lebits2int(bits[i:i+s]))

	offset = 2*8+1+3
	bIdentified = lebits2int(bits[offset:offset+1])
	offset = 27
	bSocketed = lebits2int(bits[offset:offset+1])
	offset += 1
	print("bIdentified={0},bSocketed={1}".format(bIdentified, bSocketed))
	offset += 2 + 1 + 1
	bEar = lebits2int(bits[offset:offset+1])
	offset += 1
	offset += 1 + 3
	bSimple = lebits2int(bits[offset:offset+1])
	offset += 1
	bEthereal = lebits2int(bits[offset:offset+1])
	offset += 1
	print("bEar={0},bSimple={1},bEthereal={2}".format(bEar, bSimple, bEthereal))
	offset += 1 # unk47

	bPersonalized = lebits2int(bits[offset:offset+1])
	offset += 1

	offset += 1 # unk51
	bRuneWord = lebits2int(bits[offset:offset+1])
	offset += 1
	print("bPersonalized={0},bRune={1}".format(bPersonalized, bRuneWord))
	offset += 5 # unk51

	offset = 76
	code = ''.join([chr(int(bits[offset:offset+32][i*8:i*8+8][::-1],2)) for i in range(4) ])
	offset += 32
	nGems = lebits2int(bits[offset:offset+3])
	offset += 3
	print("code={0},#gems={1}".format(code, nGems))

	guid = lebits2int(bits[offset:offset+32])
	offset += 32
	iLevel = lebits2int(bits[offset:offset+7])
	offset += 7
	print("guid=0x{0:04x},iLvl={1}".format(guid, iLevel))

	iQuality = lebits2int(bits[offset:offset+4])
	offset += 4
	print("iQuality={0}-{1}".format(iQuality, quality.byId[iQuality]))

	bVarGfx = lebits2int(bits[offset:offset+1])
	offset += 1
	if bVarGfx:
		iVarGfx = lebits2int(bits[offset:offset+3])
		offset += 3
		print("iVarGfx={0}".format(iVarGfx))

	bClass = lebits2int(bits[offset:offset+1])
	offset += 1
	if bClass:
		wClass = lebits2int(bits[offset:offset+11])
		offset += 11
		print("wClass={0}".format(wClass))

	if iQuality == quality.High:
		iQualitySubType = lebits2int(bits[offset:offset+3])
		offset += 3
		print("\tsubType={0}(0x{0:x})".format(iQualitySubType))
	elif iQuality == quality.Unique:
		iUniqId = lebits2int(bits[offset:offset+12])
		offset += 12
		print("\tUniqItem: id={0}(0x{0:x})".format(iUniqId))
	elif iQuality == quality.PartOfSet:
		iSetId = lebits2int(bits[offset:offset+12])
		offset += 12
		print("\tSetItem: id={0}(0x{0:x})".format(iSetId))
	else:
		print("\t?", iQuality)

	if bRuneWord:
		wRuneWord = lebits2int(bits[offset:offset+16])
		offset += 7 # TODO: 16 ???
		print("runeWord:", wRuneWord, "offset:", offset)

	bTimestamp = lebits2int(bits[offset:offset+1])
	offset += 1
	if bTimestamp:
		dw3 = lebits2int(bits[offset:offset+32*3])
		offset += 32 * 3
		print("dwTimestamp?=0x{0:x}".format(dw3))

	print("offset before type data", offset, bits[offset:offset+8])
	sType, typeCfg = iTypeFromCode(code)
	print("type: {0} - {1}".format(sType, typeCfg["name"]))
	if sType == "weapon":
		print("type specific:", bits[offset:offset+17], offset)
		if typeCfg["nodurability"]:
			d = bits[offset:offset+8]
			offset += 17
			print("\tdurability: INDESTRUCTIBLE(no durability, pad=0x{0:05x})".format(lebits2int(d)))
		else:
			max_durability = lebits2int(bits[offset:offset+8])
			offset += 8
			if max_durability > 0:
				durability = lebits2int(bits[offset:offset+9])
				offset += 9
				print("\tdurability: {0}/{1}".format(durability, max_durability))
			else:
				print("\tdurability: INDESTRUCTIBLE")

		# optional quantity
		if typeCfg["maxstack"] > 0:
			print("\tquantity:", lebits2int(bits[offset:offset+9]))
			offset += 9

	elif sType == "armor":
		iDefence = lebits2int(bits[offset:offset+11])
		offset += 11
		print("\tiDefence={0}".format(iDefence))

		iMaxDur = lebits2int(bits[offset:offset+8])
		offset += 8
		if iMaxDur > 0:
			iCurDur = lebits2int(bits[offset:offset+9])
			offset += 9
			print("\tdurability={0}/{1}".format(iCurDur, iMaxDur))
		else:
			print("\tIndestructible")

	# armor or weapon
	if bSocketed:
		iSockets = lebits2int(bits[offset:offset+4])
		offset += 4
		print("\tsockets: {0}".format(iSockets))

	print("offset before props data", offset, bits[offset:offset+9])
	# debug
	# old = offset
	# offset = len(bits)-pad-9-9-7-9-18 # debug
	# print("offset={0}-{1} before props".format(old, offset))
	# if old < offset:
	# 	s = bits[old:offset]
	# 	print("unread:", s, lebits2int(s))
	# ops
	if bRuneWord:
		print(">>>> props from white:")
		offset = decodeProps(bits, offset)
		print(">>>> props from Rune Word:")

	offset = decodeProps(bits, offset)

	if offset+pad != len(bits):
		print("offset:{0}+{1}/{2}".format(offset, pad, len(bits)))
	else:
		print("offset:{0}".format(offset))

if __name__ == "__main__":
	with open(sys.argv[1], "rb") as f:
		parseD2I(f.read())
