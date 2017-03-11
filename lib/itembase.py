class ItemBase:
	def __init__(self, bEar=0, bSimple=0, bEthereal=0, bSocketed=0, wVersion=0x64):
		self.bEar = bEar
		self.bSimple = bSimple
		self.bEthereal = bEthereal
		self.bSocketed = bSocketed
		self.wVersion = wVersion

	def writeStream(self, stream):
		stream.append(ord('J'), 8)
		stream.append(ord('M'), 8)
		stream.append(0, 1) # quest item?
		stream.append(0, 3) # unknown
		stream.append(1, 1) # identified?
		stream.append(0, 3) # unknown
		# :1 Diabled item, :1 unk, :1 duplicate item :1 bSocketed, :2 unk, :1 illegal equip, :1 unk
		stream.append(0, 3)
		stream.append(self.bSocketed, 1)
		stream.append(0, 4)
		# :1 bEar, :1 bStarter Item, :3 unk, :1 bSimple, :1 bEthereal 1: unk(always 1)
		stream.append(self.bEar, 1)
		stream.append(0, 4)
		stream.append(self.bSimple, 1)
		stream.append(self.bEthereal, 1)
		stream.append(1, 1)
		# :1 bPersonalized :1 unk(always0), :1 bHasRuneWord :5 unk
		stream.append(0, 8)
		stream.append(self.wVersion, 10) # :8 version(0x64 = exp)
		# :3 location, :4bits Position on body
		stream.append(0, 3)
		stream.append(0, 4)
		# :4 Grid column :4bits Grid Row
		stream.append(0, 4)
		stream.append(0, 4)
		# :3 iStored In(1 = inventory),
		stream.append(0, 3)

