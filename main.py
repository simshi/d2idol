#!/usr/bin/env python

import sys
from lib import quality

# print("under construction, please use 'make test'")
def lebits2int(bits):
	return int(bits[::-1], 2)

def parseD2I(bytes):
	bits = ''.join(["{0:08b}".format(ord(v))[::-1] for v in bytes])
	print bits
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

	if iQuality == quality.Unique:
		iUniqId = lebits2int(bits[offset:offset+12])
		offset += 12
		print("UniqItem: id={0}(0x{0:x})".format(iUniqId))
	elif iQuality == quality.PartOfSet:
		iSetId = lebits2int(bits[offset:offset+12])
		offset += 12
		print("SetItem: id={0}(0x{0:x})".format(iSetId))
	else:
		print "?", iQuality

	bTimestamp = lebits2int(bits[offset:offset+1])
	offset += 1
	if bTimestamp:
		dw3 = lebits2int(bits[offset:offset+32*3])
		offset += 32 * 3
		print("dwTimestamp[3]=0x{0:x}".format(dw3))

	# TODO: type unmarshell
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

	# optional quantity

	if bSocketed > 0:
		iSockets = lebits2int(bits[offset:offset+4])
		offset += 4
		print("iSockets={0}".format(iSockets))


if __name__ == "__main__":
	with open(sys.argv[1], "rb") as f:
		parseD2I(f.read())
