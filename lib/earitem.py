from itembase import ItemBase

class EarItem():
	def __init__(self, name, iClass = 1, iLevel = 62):
		if len(name) > 10:
			raise ValueError("assert(len(name) <= 10)")

		self.name = name
		self.iClass = iClass
		self.iLevel = iLevel
		self.base = ItemBase(bSimple=1, bEar=1)

	def writeStream(self, stream):
		self.base.writeStream(stream)

		stream.append(self.iClass, 3)
		stream.append(self.iLevel, 7)

		for c in self.name:
			stream.append(ord(c), 7)

		stream.append(0, 7)

