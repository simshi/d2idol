from .import itemtype
from .import quality
from .itemprops import ItemProps

class SetItem:
	def __init__(self, code="7ws ", setId=0x53):
		self.code = code
		self.setId = setId
		self.nGems = 0
		self.guid = 0x0000ff00 # as color 'green' ^_^
		self.bClass = 0
		self.wClass = 1
		self.props = ItemProps()
		self.setProps = [ItemProps() for _ in range(5)]
		self.type = itemtype.createByCode(code)
		self.base = self.type.createBase()

	def addProp(self, id, *args):
		return self.props.add(id, *args)

	def addPropGroup(self, group):
		self.props.addGroup(group)

	def addSetProp(self, index, id, *args):
		self.setProps[index].add(id, *args)

	def writeStream(self, stream):
		self.base.writeStream(stream)

		stream.appendString(self.code)

		stream.append(self.nGems, 3)
		stream.append(self.guid, 32)
		stream.append(1, 7) # iLevel

		stream.append(quality.PartOfSet, 4)

		stream.append(0, 1) # assume always bVarGfx==0
		stream.append(self.bClass, 1)
		if self.bClass:
			stream.append(self.wClass, 11)

		stream.append(self.setId, 12)

		stream.append(0, 1) # no Timestamp

		self.type.writeStream(stream)

		for p in self.setProps:
			stream.append(len(p) > 0 and 1 or 0, 1)

		self.props.writeStream(stream)

		for p in self.setProps:
			if len(p) > 0:
				p.writeStream(stream)
