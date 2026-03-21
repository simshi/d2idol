from .quality_item import QualityItem
from .import quality

class UniqItem(QualityItem):
	def __init__(self, code="amu ", uniqId=25):
		super().__init__(code, quality.Unique, uniqId, guid=0x04030211)
