from .itembase import ItemBase
from . import quality
from .itemprops import ItemProps

class Charm():
	def __init__(self, code="cm1 ", wSuffix=0x115):
		self.base = ItemBase(wVersion=0x65)
		self.code = code
		self.wSuffix = wSuffix
		self.nGems = 0
		self.guid = 0x04030201
		self.bVarGfx = 0
		self.iVarGfx = 0
		self.bClass = 0
		self.wClass = 1
		self.props = ItemProps()

	def setGfx(self, iVarGfx):
		self.bVarGfx = True
		self.iVarGfx = iVarGfx

	def addProp(self, id, *args):
		return self.props.add(id, *args)

	def writeStream(self, stream):
		self.base.writeStream(stream)

		stream.appendString(self.code)

		stream.append(self.nGems, 3)
		stream.append(self.guid, 32)
		stream.append(1, 7) # iLevel

		stream.append(quality.Magic, 4)

		stream.append(self.bVarGfx, 1)
		if self.bVarGfx:
			stream.append(self.iVarGfx, 3)

		stream.append(self.bClass, 1)
		if self.bClass:
			stream.append(self.wClass, 11)

		stream.append(0, 11)
		stream.append(self.wSuffix, 11)

		stream.append(0, 1) # no Timestamp

		self.props.writeStream(stream)
