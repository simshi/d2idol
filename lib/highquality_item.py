from .import itemtype
from .import quality
from .itemprops import ItemProps

class HighQualityItem:
	def __init__(self, code="amu ", nSockets=99, subType=0):
		self.code = code
		self.nGems = 0
		self.guid = 0x04030211 * nSockets
		# FIXME: max sockets depends on item type and item level
		self.iLevel = 88
		# if nSockets < 99:
		# 	if nSockets >= 6:
		# 		self.iLevel = 44
		# 	elif nSockets >= 5:
		# 		self.iLevel = 34 # not sure
		# 	elif nSockets >= 4:
		# 		self.iLevel = 34 # not sure
		self.bClass = 0
		self.wClass = 1
		self.subType = subType
		self.props = ItemProps()
		self.type = itemtype.createByCode(code, nSockets)
		self.base = self.type.createBase()

	def addProp(self, id, *args):
		return self.props.add(id, *args)

	def addPropGroup(self, group):
		self.props.addGroup(group)

	def writeStream(self, stream):
		self.base.writeStream(stream)

		# type code
		stream.appendString(self.code)

		stream.append(self.nGems, 3)
		stream.append(self.guid, 32)
		stream.append(self.iLevel, 7) # iLevel

		stream.append(quality.High, 4)

		stream.append(0, 1) # assume item bVarGfx==0
		stream.append(0, 1) # bClass = 0
		if self.bClass:
			stream.append(self.wClass, 11)

		# quality specific
		stream.append(self.subType, 3)

		# timestamp seems incorrect!!!
		stream.append(0, 1) # no Timestamp
		# with timestamp
		# stream.append(1, 1)
		# stream.append(0xf9b94161, 32)
		# stream.append(0x3c1e1140, 32)
		# stream.append(0x7fc03098, 32)

		self.type.writeStream(stream)

		self.props.writeStream(stream)
