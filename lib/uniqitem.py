import itemtype
import quality
from itemprops import ItemProps

class UniqItem:
	def __init__(self, code="amu ", uniqId=25):
		self.code = code
		self.uniqId = uniqId
		self.nGems = 0
		self.guid = 0x04030211
		self.bClass = 0
		self.wClass = 1
		self.props = ItemProps()
		self.type = itemtype.createByCode(code)
		self.base = self.type.createBase()

	def addProp(self, id, *args):
		return self.props.add(id, *args)

	def addPropGroup(self, group):
		self.props.addGroup(group)

	def writeStream(self, stream):
		self.base.writeStream(stream)

		stream.appendString(self.code)

		stream.append(self.nGems, 3)
		stream.append(self.guid, 32)
		stream.append(1, 7) # iLevel

		stream.append(quality.Unique, 4)

		stream.append(0, 1) # assume uniq item bVarGfx==0
		stream.append(self.bClass, 1)
		if self.bClass:
			stream.append(self.wClass, 11)

		stream.append(self.uniqId, 12)

		stream.append(0, 1) # no Timestamp

		self.type.writeStream(stream)

		self.props.writeStream(stream)
