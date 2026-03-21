from .import itemtype
from .itemprops import ItemProps

class QualityItem:
	def __init__(self, code, qualityVal, itemId, guid=0):
		self.code = code
		self.qualityVal = qualityVal
		self.itemId = itemId
		self.nGems = 0
		self.guid = guid
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
		stream.append(1, 7)

		stream.append(self.qualityVal, 4)

		stream.append(0, 1)
		stream.append(self.bClass, 1)
		if self.bClass:
			stream.append(self.wClass, 11)

		stream.append(self.itemId, 12)

		stream.append(0, 1)

		self.type.writeStream(stream)

		self._writeExtraData(stream)

		self.props.writeStream(stream)

		self._writeExtraProps(stream)

	def _writeExtraData(self, stream):
		pass

	def _writeExtraProps(self, stream):
		pass
