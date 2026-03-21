from .quality_item import QualityItem
from .import quality
from .itemprops import ItemProps

class SetItem(QualityItem):
	def __init__(self, code="7ws ", setId=0x53):
		super().__init__(code, quality.PartOfSet, setId, guid=0x0000ff00)
		self.setProps = [ItemProps() for _ in range(5)]

	def addSetProp(self, index, id, *args):
		self.setProps[index].add(id, *args)

	def _writeExtraData(self, stream):
		for p in self.setProps:
			stream.append(len(p) > 0 and 1 or 0, 1)

	def _writeExtraProps(self, stream):
		for p in self.setProps:
			if len(p) > 0:
				p.writeStream(stream)
