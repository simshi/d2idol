from collections import namedtuple
from enum import Enum

from .skill_data import getSkillName, getSkillTreeName, getSkillSetName


class Ptn(Enum):
	NONE = 0
	RAW = 1			#%d, val[i]
	CLASS = 2		#%s, GetClassName(val[i])
	SKILL = 3		#%s, GetSkillName(val[i])
	SKILL_TREE = 4	#%s, GetSkillTreeName(val[i])
	SKILL_SET = 5	#%s, GetSkillSetName(val[i])
	DURATION = 6	#%d, val[i]/25
	TIME = 7		#%s, GetTimeDesc(val[i])
	IGNORE = 8		#skip this value

	def __str__(self):
		return self.name.lower()


PropDef = namedtuple('PropDef', ['bits', 'base', 'fmt', 'ptns'])

arrPropTbl=[
	PropDef([8,0,0,0], 32, "+%d to Strength", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 32, "+%d to Energy", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 32, "+%d to Dexterity", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 32, "+%d to Vitality", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 32, "+%d to Life", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 32, "+%d to Mana", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 32, "+%d to Maximum Stamina", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 0, "+%d%% Enhanced Defense", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#16
	PropDef([9,9,0,0], 0, "+{0}%-{1}% Enhanced Damage", [Ptn.RAW,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#17
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([10,0,0,0], 0, "+{0} to Attack Rating", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#19
	PropDef([6,0,0,0], 0, "%d%% Increased Chance of Blocking", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Minimum Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "+%d to Maximum Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to 2h Minimum Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "+%d to 2h Maximum Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 0, "Regenerate Mana %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 0, "Heal Stamina %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([11,0,0,0], 10, "+%d Defense", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#31
	PropDef([9,0,0,0], 10, "+%d Defense vs. Missile", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 10, "+%d Defense vs. Melee", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Damage Reduced by %d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Magic Damage Reduced by %d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 0, "Damage Reduced by %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 50, "Magic Resist +%d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "+%d%% to Maximum Magic Resist", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 50, "Fire Resist +%d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#39
	PropDef([5,0,0,0], 0, "+%d%% to Maximum Fire Resist", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 50, "Lightning Resist +%d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "+%d%% to Maximum Lightning Resist", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 50, "Cold Resist +%d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "+%d%% to Maximum Cold Resist", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 50, "Poison Resist +%d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "+%d%% to Maximum Poison Resist", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#46
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,9,0,0], 0, "Adds %d-%d fire damage", [Ptn.RAW,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#48
	PropDef([9,0,0,0], 0, "Adds %d fire damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#49
	PropDef([6,10,0,0], 0, "Adds %d-%d lightning damage", [Ptn.RAW,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#50
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,9,0,0], 0, "Adds {0}-{1} magic damage", [Ptn.RAW,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#52
	PropDef([9,0,0,0], 0, "Adds {0} magic damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#53
	PropDef([8,9,8,0], 0, "Adds %d-%d cold damage over %d sec", [Ptn.RAW,Ptn.RAW,Ptn.DURATION,Ptn.NONE]),	#54
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([10,10,9,0], 0, "Adds %d-%d poison damage over %d seconds", [Ptn.RAW,Ptn.RAW,Ptn.DURATION,Ptn.NONE]),	#57
	PropDef([10,0,0,0], 0, "Adds %d poison damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#58
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "{0}% Life stolen per hit", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#60
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "{0}% Mana stolen per hit", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#62
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 30, "%d%% Faster Run/Walk", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#67
	PropDef([7,0,0,0], 30, "%d%% Increased Attack Speed", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 30, "+%d Maximum Durability", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#73
	PropDef([6,0,0,0], 30, "Replenish Life +%d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#74
	PropDef([7,0,0,0], 20, "Increase Maximum Durability X%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 10, "Increase Maximum Life %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 10, "Increase Maximum Mana %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Attacker Takes Damage of %d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 100, "%d%% Extra Gold from Monsters", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#79
	PropDef([8,0,0,0], 100, "%d%% Better Chance of Getting Magic Items", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Knockback", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#81
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([3,3,0,0], 0, "+%d to %s Skill Levels", [Ptn.RAW,Ptn.CLASS,Ptn.NONE,Ptn.NONE]),	#83
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 50, "+%d%% to Experience Gained", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#85
	PropDef([7,0,0,0], 0, "+%d Life after each Kill", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#86
	PropDef([7,0,0,0], 0, "Reduces All Vendor Prices %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#87
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([4,0,0,0], 4, "+%d to Light Radius", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#89
	PropDef([5,0,0,0], 0, "Its effect is to alter the color of the ambient light", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([8,0,0,0], 100, "Requirements %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#91
	PropDef([7,0,0,0], 0, "Requirements Level +%d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#92
	PropDef([7,0,0,0], 20, "%d%% Increased Attack Speed", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#93
	PropDef([7,0,0,0], 64, "Requirements Level %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#94
	PropDef([0,0,0,0], 0, "N/A", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 20, "%d%% Faster Run/Walk", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#96
	PropDef([9,6,0,0], 0, "Skill %s +%d", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#97, add non-class skill points
	PropDef([8,0,0,0], 100, "State %d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#98
	PropDef([7,0,0,0], 20, "%d%% Faster Hit Recovery", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#99
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 20, "%d%% Faster Block Rate", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#102
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 20, "%d%% Faster Cast Rate", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#105
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,3,0,0], 0, "%s +%d(character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#107
	PropDef([1,0,0,0], 0, "Slain Monsters Rest In Peace", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#108
	PropDef([9,5,0,0], 0, "+%d to %s (character class Only)", [Ptn.RAW,Ptn.SKILL,Ptn.NONE,Ptn.NONE]),	#109 ??
	PropDef([8,0,0,0], 20, "Poison Length Reduced by %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#110
	PropDef([9,0,0,0], 20, "Damage +%d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#111
	[[7,0,0,0], -1, "Hit Causes Monster to Flee %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]],
	PropDef([7,0,0,0], 0, "Hit Blinds Target +%d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "%d%% Damage Taken Goes to Mana", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([1,0,0,0], 0, "Ignore Target Defense", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#115
	PropDef([7,0,0,0], 0, "%d%% Target Defense", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Prevent Monster Heal", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([1,0,0,0], 0, "Half Freeze Duration", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 20, "{0}% to Attack Rating", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#119
	PropDef([7,0,0,0], 128, "%d to Monster Defense Per Hit", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 20, "+%d%% Damage to Demons", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([9,0,0,0], 20, "+%d%% Damage to Undead", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([10,0,0,0], 128, "+%d to Attack Rating against Demons", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#123
	PropDef([10,0,0,0], 128, "+%d to Attack Rating against Undead", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#124
	PropDef([1,0,0,0], 0, "Throwable", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#125
	PropDef([3,3,0,0], 0, "%+d to %s Skills", [Ptn.SKILL_TREE,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#126
	PropDef([3,0,0,0], 0, "+%d to All Skill Levels", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "Attacker Takes Lightning Damage of %d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#128
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "Freezes Target %d", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#134
	PropDef([7,0,0,0], 0, "{0}% Chance of Open Wounds", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#135
	PropDef([7,0,0,0], 0, "{0}% Chance of Crushing Blow", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#136
	PropDef([7,0,0,0], 0, "+%d Kick Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "+%d to Mana After Each Kill", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#138
	PropDef([7,0,0,0], 0, "+%d Life after each Demon Kill", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "%d%% Extra Bloody", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#140
	PropDef([7,0,0,0], 0, "%d%% Deadly Strike", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Fire Absorb %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#142
	PropDef([7,0,0,0], 0, "%d Fire Absorb", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Lightning Absorb %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "%d Lightning Absorb", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Magic Absorb %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "%d Magic Absorb", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Cold Absorb %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "%d Cold Absorb", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "Slows Target by %d%%", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#150
	PropDef([9,5,0,0], 0, "Add %s Aura (Level %d) When Equipped", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#151
	PropDef([1,0,0,0], 0, "Indestructible", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#152
	PropDef([1,0,0,0], 0, "Cannot Be Frozen", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 20, "%d%% Slower Stamina Drain", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([10,7,0,0], 0, "%d%% Reanimate As: %d", [Ptn.RAW,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#155, monster id
	PropDef([7,0,0,0], 0, "Piercing Attack (%d)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#156
	PropDef([7,0,0,0], 0, "Fires Magic Arrows (%d)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#157
	PropDef([7,0,0,0], 0, "Fires Explosive Arrows or Bolts (%d)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Minimum Throw Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([7,0,0,0], 0, "+%d to Maximum Throw Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#160
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	#seems there are no 179~187 in 1.10!!!
	PropDef([3,0,0,0], 0, "+%d to Druid Skill Levels", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#179
	PropDef([3,0,0,0], 0, "+%d to Assassin Skill Levels", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#180
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#181
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#182
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#183
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#184
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#185
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#186
	PropDef([9,5,0,0], 0, "%s +%d (character class Only)", [Ptn.SKILL,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#187
	PropDef([16,3,0,0], 0, "Skill Set %s +%d (character class Only)", [Ptn.SKILL_SET,Ptn.RAW,Ptn.NONE,Ptn.NONE]),	#188
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([4,0,0,0], 0, "Adds %d extra sockets to the item.", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#194
	PropDef([6,10,7,0], 0, "cast level {0} {1} {2}% Chance on attack", [Ptn.RAW,Ptn.SKILL,Ptn.RAW,Ptn.NONE]),	#195
	PropDef([6,10,7,0], 0, "cast {0} (level {1}, {2}% Chance) on kill", [Ptn.SKILL,Ptn.RAW,Ptn.RAW,Ptn.NONE]),	#196
	PropDef([6,10,7,0], 0, "cast {0} (level {1}, {2}% Chance) on death", [Ptn.SKILL,Ptn.RAW,Ptn.RAW,Ptn.NONE]),	#197
	PropDef([6,10,7,0], 0, "cast level {0} {1} {2}% Chance on striking", [Ptn.RAW,Ptn.SKILL,Ptn.RAW,Ptn.NONE]),#198
	PropDef([6,10,7,0], 0, "cast {0} (level {1}, {2}% Chance) on level up", [Ptn.SKILL,Ptn.RAW,Ptn.RAW,Ptn.NONE]),#199
	PropDef([6,10,7,0], 0, "+{0}% Chance to cast level {1} {2} on striking", [Ptn.RAW,Ptn.RAW,Ptn.SKILL,Ptn.NONE]),#200 ??
	PropDef([6,10,7,0], 0, "cast level {0} {1} {2}% Chance when struck", [Ptn.RAW,Ptn.SKILL,Ptn.RAW,Ptn.NONE]),#201
	PropDef([9,5,7,0], 0, "+{0}% Chance to cast level {1} {2} when struck", [Ptn.RAW,Ptn.RAW,Ptn.SKILL,Ptn.NONE]),#??
	PropDef([9,5,7,0], 0, "+{0}% Chance to cast level {1} {2} when struck", [Ptn.RAW,Ptn.RAW,Ptn.SKILL,Ptn.NONE]),#203 ??
	PropDef([6,10,8,8], 0, "{0} (level {1}, {2}/{3} Charges)", [Ptn.SKILL,Ptn.RAW,Ptn.RAW,Ptn.RAW]),	#204
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#213
	PropDef([6,0,0,0], 0, "+%d to Defense (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#214
	PropDef([6,0,0,0], 0, "%d%% Enhanced Defense (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Life (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Mana (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+{0} to Maximum Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#218
	PropDef([6,0,0,0], 0, "+{0}% Enhanced Maximum Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#219
	PropDef([6,0,0,0], 0, "+%d to Strength (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#220
	PropDef([6,0,0,0], 0, "+%d to Dexterity (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Energy (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Vitality (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d to Attack Rating (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "%d%% Bonus to Attack Rating (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d Cold Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#226
	PropDef([6,0,0,0], 0, "+%d Fire Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d Lightning Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d Poison Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Cold Resist +%d%% (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#230
	PropDef([6,0,0,0], 0, "Fire Resist +%d%% (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Lightning Resist +%d%% (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Poison Resist +%d%% (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d%% Cold Absorb (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#234
	PropDef([6,0,0,0], 0, "+%d%% Fire Absorb (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d%% Lightning Absorb (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d%% Poison Absorb (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([5,0,0,0], 0, "Attacker Takes Damage of %d (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#238
	PropDef([6,0,0,0], 0, "%d%% Extra Gold from Monsters (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#239
	PropDef([6,0,0,0], 0, "%d%% Better Chance of Getting Magic Items (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Heal Stamina Plus %d%% (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Stamina +%d (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#242
	PropDef([6,0,0,0], 0, "%d%% Damage to Demons (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#243
	PropDef([6,0,0,0], 0, "%d%% Damage to Undead (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d%% to Attack Rating against Demons (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d%% to Attack Rating against Undead (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "%d%% Chance of Crushing Blow (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "%d%% Chance of Open Wounds (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "+%d% Kick Damage (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "%d%% to Deadly Strike (Based on Character Level)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#250
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([6,0,0,0], 0, "Repairs 1 durability in %d seconds", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#252
	PropDef([6,0,0,0], 0, "Replenishes Quantity (1 in %d seconds)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#??
	PropDef([8,0,0,0], 0, "Increased Stack Size (%d)", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#254
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#255
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#267
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Defense", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),	#268
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Enhanced Defense", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Life", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Mana", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Enhanced Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Strength", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Dexterity", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Energy", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Vitality", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Enhanced Attack Rating", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Attack Rating", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Cold Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Fire Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Lightning Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Poison Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Cold Resist", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Fire Resist", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Lightning Resist", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Poison Resist", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Cold Absorb", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Fire Absorb", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Lightning Absorb", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Poison Absorb", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Extra Gold from Monsters", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Better Chance of Getting Magic Items", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) Heal Stamina Plus %d%%-%d%%", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Stamina", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Damage to Demons", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Damage to Undead", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Attack Rating against Demons", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d to Attack Rating against Undead", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Chance of Crushing Blow", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Chance of Open Wounds", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) +%d-%d Kick Damage", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Deadly Strike", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),	#303
	PropDef([2,10,10,0], 0, "(Increases %s) %d%%-%d%% Gem Find", [Ptn.TIME,Ptn.RAW,Ptn.RAW,Ptn.NONE]),	#304
	PropDef([8,0,0,0], 50, "%d%% to Enemy Cold Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#305
	PropDef([8,0,0,0], 50, "%d%% to Enemy Fire Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#306
	PropDef([8,0,0,0], 50, "%d%% to Enemy Lightning Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#307
	PropDef([8,0,0,0], 50, "%d%% to Enemy Poison Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#308
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#310
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#320
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),
	PropDef([0,0,0,0], 0, "N/A", [Ptn.NONE,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#328
	PropDef([9,0,0,0], 50, "+%d to Fire Skill Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#329
	PropDef([9,0,0,0], 50, "+%d to Lightning Skill Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#330
	PropDef([9,0,0,0], 50, "+%d to Cold Skill Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#331
	PropDef([9,0,0,0], 50, "+%d to Poison Skill Damage", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#332
	PropDef([8,0,0,0], 0, "%d%% to Enemy Cold Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#333
	PropDef([8,0,0,0], 0, "%d%% to Enemy Fire Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#334
	PropDef([8,0,0,0], 0, "%d%% to Enemy Lightning Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#335
	PropDef([8,0,0,0], 0, "%d%% to Enemy Poison Resistance", [Ptn.RAW,Ptn.NONE,Ptn.NONE,Ptn.NONE]),	#336
]

def getPropFromID(id):
	return arrPropTbl[id]
