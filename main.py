#!/usr/bin/env python

import sys
from lib import quality
from lib.itemprops import getPropFromID
from lib.itemtype import iTypeFromCode
import lib.itemprops as itemprops

# print("under construction, please use 'make test'")
def lebits2int(bits):
	return int(bits[::-1], 2)

def parseD2I(bytes):
	bits = ''.join(["{0:08b}".format(ord(v))[::-1] for v in bytes])
	print(bits)
	pad = 0
	for v in bits[-7:]:
		if v == '0':
			pad += 1
	print("pad={0}/{1}".format(pad, len(bits)), bits[-7:])

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
		iClass = lebits2int(bits[offset:offset+11])
		offset += 11
		print("iClass={0}".format(iClass))

	if iQuality == quality.High:
		iQualitySubType = lebits2int(bits[offset:offset+3])
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

	# TODO: unclear
	print("offset before timestamp?", offset, bits[offset:offset+4])
	bTimestamp = lebits2int(bits[offset:offset+1])
	offset += 1
	if bTimestamp:
		# dw3 = lebits2int(bits[offset:offset+32*3])
		# offset += 32 * 3
		dw3 = lebits2int(bits[offset:offset+3])
		offset += 3
		print("dwTimestamp?=0x{0:x}".format(dw3))
	else:
		print("no timestamp?", bits[offset:offset+3])
		offset += 3

	print("offset before type data", offset, bits[offset:offset+8])
	# TODO: type unmarshell
	iType = iTypeFromCode(code)
	print("type:{0}".format(iType))
	if iType == "weapon":
		print("type specific:", bits[offset:offset+17], offset)
		max_durability = lebits2int(bits[offset:offset+8])
		offset += 8
		if max_durability > 0:
			durability = lebits2int(bits[offset:offset+9])
			offset += 9
			print("\tdurability: {0}/{1}".format(durability, max_durability))
		else:
			print("\tdurability: INDESTRUCTIBLE")

		# optional quantity
		# type = getTypeFromCode(code)

	elif iType == "armor":
		iDefence = lebits2int(bits[offset:offset+11])
		offset += 11
		print("iDefence={0}".format(iDefence))

		iMaxDur = lebits2int(bits[offset:offset+8])
		offset += 8
		if iMaxDur > 0:
			iCurDur = lebits2int(bits[offset:offset+9])
			offset += 9
			print("durability={0}/{1}".format(iCurDur, iMaxDur))
		else:
			print("Indestructible")

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
				print("raw={0}".format(v))
			elif ptn == itemprops.ptnSkill:
				print("skill={0}".format(v))
			elif ptn == itemprops.ptnSkillTree:
				print("skillTree={0}".format(v))
			elif ptn == itemprops.ptnClass:
				print("class={0}".format(v))
			elif ptn == itemprops.ptnDuration:
				print("duration={0}".format(v))
			elif ptn == itemprops.ptnTime:
				print("time={0}".format(v))
			i += 1
	if offset+pad != len(bits):
		print("offset:{0}+{1}/{2}".format(offset, pad, len(bits)))
	else:
		print("offset:{0}".format(offset))

if __name__ == "__main__":
	with open(sys.argv[1], "rb") as f:
		parseD2I(f.read())
