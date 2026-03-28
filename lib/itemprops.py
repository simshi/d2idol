from dataclasses import dataclass
from typing import List, Optional

from .prop import (
	Ptn,
	arrPropTbl,
	getPropFromID,
	getSkillName,
	getSkillTreeName,
	getSkillSetName,
)


@dataclass
class PropDetail:
	bits: int
	ptn: str
	value: int
	base: Optional[int] = None
	name: Optional[str] = None


@dataclass
class PropResult:
	id: int
	formatted: Optional[str]
	details: List[PropDetail]


_propGroups = {
	"characteristic": [
		0, 1, 2, 3,
		7, #+%d to Life
		9, #+%d to Mana
		# 11, #+%d to Maximum Stamina
		76, #Max life +x%
		# 127, # +7 (3 bits) to All Skill Level
	], "mf": [
		80, #MF +x%
		240, #MF +d% per level
	], "greed": [
		79, #Extra Gold +x%
		239, #extra gold +dd per level
	], "magicfind": [
		79, #Extra Gold +x%
		80, #MF +x%
		239, #extra gold +dd per level
		240, #MF +d% per level
	], "basicdefense": [
		16,31, # + defence
		# 34,36, # dmg reduce
		214, #+%d to Defense (Based on Character Level)
		215, #%d%% Enhanced Defense (Based on Character Level)
	], "allresist": [
		37, #Magic Resist +%d%%
		39, #Fire Resist +%d%%
		41, #Lightning Resist +%d%%
		43, #Cold Resist +%d%%
		45, #Poison Resist +%d%%
	], "defense": [
		16,31,32,33, # + defence
		34,35,36, # dmg reduce
		37,38, #magic resist
		39,40, #fire resist
		41,42, #Lightning Resist
		43,44, #Cold Resist
		45,46, #Poison Resist
		74, #Replenish Life +%d
		76,77, #Max life/mana +x%
		# 78, #Attacker Takes Damage of %d
		# 81, #Knockback
		86, #+x life after each kill
		110, #Poison Length -x%
		118, #Half Freeze Duration
		214, #+%d to Defense (Based on Character Level)
		215, #%d%% Enhanced Defense (Based on Character Level)
	], "basicoffense": [
		17, #+%d-%d Enhanced Damage
		19, #+%d to Attack Rating
		60, #+% life stolen per hit
		62, #+% mana stolen per hit
		93, #%d%% Increased Attack Speed
		111, #Damage +%d
		115, #Ignore Target Defense
		141, #+d Deadly Strike
	], "offense": [
		17, #+%d-%d Enhanced Damage
		19, #+%d to Attack Rating
		48, #Adds %d-%d fire damage
		49, #Adds %d fire damage
		50, #Adds %d-%d lightning damage
		52, #Adds %d-%d magic damage
		53, #Adds %d magic damage
		# 54, #Adds %d-%d cold damage over %d sec ==> leaves no corpse?
		57, #Adds %d-%d poison damage over %d seconds
		58, #Adds %d poison damage
		60, #+% life stolen per hit
		62, #+% mana stolen per hit
		93, #%d%% Increased Attack Speed
		#105, #%d%% Faster Cast Rate
		#108, #Slain Monsters Rest In Peace
		111, #Damage +%d
		#113, #Hit Blinds Target +%d
		115, #Ignore Target Defense
		#117, #Prevent Monster Heal
		119, #%d%% to Attack Rating
		#121, #+%d%% Damage to Demons
		#122, #+%d%% Damage to Undead
		#123, #+%d to Attack Rating against Demons
		#124, #+%d to Attack Rating against Undead
		# 134, #Freezes Target %d ==> leaves no corpse?
		135, #%d%% Chance of Open Wounds
		136, #%d%% Chance of Crushing Blow
		#137, #+%d Kick Damage
		141, #+d Deadly Strike,
		218, #+%d to Maximum Damage (Based on Character Level)
		219, #%d%% Enhanced Maximum Damage (Based on Character Level)
	]
}


class ItemProps:
	def __init__(self):
		self._props = {}
		self._nonClassSkills = []
		self._all_resistance = set()

	def __len__(self):
		return sum(map(len, (self._props, self._nonClassSkills, self._all_resistance)))

	def add(self, id, p0=0xffff, p1=0xffff, p2=0xffff, p3=0xffff):
		if id == 97:
			self._nonClassSkills.append([p0, p1, p2, p3])
			return

		# TODO: how to aggrate to 'all resist'?
		if id in [39, 41, 43, 45]:
			self._all_resistance.add(id)
			return

		self._props[id] = [p0, p1, p2, p3]

	def addGroup(self, group):
		for id in _propGroups[group]:
			self.add(id, 0xffff, 0xffff, 0xffff, 0xffff)

	def writeStream(self, stream):
		for id in sorted(self._props):
			stream.append(id, 9)
			stream.append(self._props[id][0], arrPropTbl[id].bits[0])
			stream.append(self._props[id][1], arrPropTbl[id].bits[1])
			stream.append(self._props[id][2], arrPropTbl[id].bits[2])
			stream.append(self._props[id][3], arrPropTbl[id].bits[3])

		for v in self._nonClassSkills:
			stream.append(97, 9)
			stream.append(v[0], arrPropTbl[97].bits[0])
			stream.append(v[1], arrPropTbl[97].bits[1])
			stream.append(v[2], arrPropTbl[97].bits[2])
			stream.append(v[3], arrPropTbl[97].bits[3])

		for id in sorted(self._all_resistance):
			stream.append(id, 9)
			stream.append(0xff, 8)

		stream.append(0x1ff, 9)


def decodeProp(stream) -> Optional[PropResult]:
	id = stream.read(9)
	if id == 0x1ff:
		return None

	prop = getPropFromID(id)
	bits_config = prop.bits
	base_value = prop.base
	format_template = prop.fmt
	ptn_config = prop.ptns

	details: List[PropDetail] = []
	params = []

	for i, n in enumerate(bits_config):
		if n == 0:
			break

		raw_value = stream.read(n)
		value = raw_value

		if base_value > 0:
			value = raw_value - base_value

		ptn = ptn_config[i]
		detail_base = base_value if base_value > 0 else None

		detail_name = None
		if ptn == Ptn.RAW:
			params.append(value)
		elif ptn == Ptn.SKILL:
			skill_name = getSkillName(value)
			params.append(skill_name)
			detail_name = skill_name
		elif ptn == Ptn.SKILL_TREE:
			tree_name = getSkillTreeName(value)
			params.append(tree_name)
			detail_name = tree_name
		elif ptn == Ptn.SKILL_SET:
			set_name = getSkillSetName(value)
			params.append(set_name)
			detail_name = set_name
		elif ptn == Ptn.CLASS:
			params.append(value)
		elif ptn == Ptn.DURATION:
			params.append(value)
		elif ptn == Ptn.TIME:
			params.append(value)
		elif ptn == Ptn.NONE:
			pass

		details.append(PropDetail(
			bits=n,
			ptn=str(ptn),
			value=raw_value,
			base=detail_base,
			name=detail_name,
		))

	formatted = None
	if format_template:
		if params:
			try:
				if "{0" in format_template:
					formatted = format_template.format(*params)
				else:
					formatted = format_template % tuple(params)
			except Exception:
				formatted = format_template
		else:
			formatted = format_template

	return PropResult(
		id=id,
		formatted=formatted,
		details=details,
	)

