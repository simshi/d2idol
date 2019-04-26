ptnNone = 1
ptnRaw = 2			#%d, val[i]
ptnSkill = 3		#%s, GetSkillName(val[i])
ptnSkillTree = 4	#%s, GetSkillTreeName(val[i])
ptnClass = 5		#%s, GetClassName(val[i])
ptnDuration = 6	#%d, val[i]/25
ptnTime = 7		#%s, GetTimeDesc(val[i])
ptnIgnore = 8		#skip this value

arrPropTbl=[
	[[8,0,0,0], 32, "+%d to Strength",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 32, "+%d to Energy",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 32, "+%d to Dexterity",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 32, "+%d to Vitality",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 32, "+%d to Life",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 32, "+%d to Mana",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 32, "+%d to Maximum Stamina",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 0, "+%d%% Enhanced Defense", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#16
	[[9,9,0,0], 0, "+%d%%-%d%% Enhanced Damage", [ptnRaw,ptnRaw,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[10,0,0,0], 0, "+%d to Attack Rating",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% Increased Chance of Blocking", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Minimum Damage",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "+%d to Maximum Damage",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to 2h Minimum Damage",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "+%d to 2h Maximum Damage",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Regenerate Mana %d%%",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Heal Stamina %d%%",		[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[11,0,0,0], 10, "+%d Defense", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#31
	[[9,0,0,0], 10, "+%d Defense vs. Missile",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 10, "+%d Defense vs. Melee",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Damage Reduced by %d",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Magic Damage Reduced by %d",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Damage Reduced by %d%%",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Magic Resist +%d%%",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "+%d%% to Maximum Magic Resist", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Fire Resist +%d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#39
	[[5,0,0,0], 0, "+%d%% to Maximum Fire Resist",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Lightning Resist +%d%%",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "+%d%% to Maximum Lightning Resist",	[ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Cold Resist +%d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "+%d%% to Maximum Cold Resist", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 0, "Poison Resist +%d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "+%d%% to Maximum Poison Resist", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#46
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,9,0,0], 0, "Adds %d-%d fire damage", [ptnRaw,ptnRaw,ptnNone,ptnNone]],	#48
	[[9,0,0,0], 0, "Adds %d fire damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#49
	[[6,10,0,0], 0, "Adds %d-%d lightning damage", [ptnRaw,ptnRaw,ptnNone,ptnNone]],	#50
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,9,0,0], 0, "Adds %d-%d magic damage", [ptnRaw,ptnRaw,ptnNone,ptnNone]],	#52
	[[9,0,0,0], 0, "Adds %d magic damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#53
	[[8,9,8,0], 0, "Adds %d-%d cold damage over %d sec", [ptnRaw,ptnRaw,ptnDuration,ptnNone]],	#54
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[10,10,9,0], 0, "Adds %d-%d poison damage over %d seconds", [ptnRaw,ptnRaw,ptnDuration,ptnNone]],	#57
	[[10,0,0,0], 0, "Adds %d poison damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#58
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d%% Life stolen per hit", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#60
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d%% Mana stolen per hit", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#62
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 30, "%d%% Faster Run/Walk", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#67
	[[7,0,0,0], 30, "%d%% Increased Attack Speed", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 30, "+%d Maximum Durability", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#73
	[[6,0,0,0], 30, "Replenish Life +%d", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#74
	[[7,0,0,0], 20, "Increase Maximum Durability X%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 10, "Increase Maximum Life %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 10, "Increase Maximum Mana %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Attacker Takes Damage of %d", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 100, "%d%% Extra Gold from Monsters", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#79
	[[8,0,0,0], 100, "%d%% Better Chance of Getting Magic Items", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Knockback", [ptnNone,ptnNone,ptnNone,ptnNone]],	#81
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[3,3,0,0], 0, "+%d to %s Skill Levels", [ptnRaw,ptnClass,ptnNone,ptnNone]],	#83
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 50, "+%d%% to Experience Gained", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#85
	[[7,0,0,0], 0, "+%d Life after each Kill", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#86
	[[7,0,0,0], 0, "Reduces All Vendor Prices %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#87
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[4,0,0,0], 4, "+%d to Light Radius", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#89
	[[5,0,0,0], 0, "Its effect is to alter the color of the ambient light", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[8,0,0,0], 100, "Requirements %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#91
	[[7,0,0,0], 0, "Requirements Level +%d", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#92
	[[7,0,0,0], 20, "%d%% Increased Attack Speed", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#93
	[[7,0,0,0], 64, "Requirements Level %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#94
	[[0,0,0,0], 0, "N/A", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 20, "%d%% Faster Run/Walk", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#96
	[[9,6,0,0], 100, "+%d to Skill %s", [ptnRaw,ptnSkill,ptnNone,ptnNone]],	#97, add non-class skill points
	[[8,0,0,0], 100, "State %d", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#98
	[[7,0,0,0], 20, "%d%% Faster Hit Recovery", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#99
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 20, "%d%% Faster Block Rate", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#102
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 20, "%d%% Faster Cast Rate", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#105
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[9,3,0,0], 0, "%s +%d(character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#107
	[[1,0,0,0], 0, "Slain Monsters Rest In Peace", [ptnNone,ptnNone,ptnNone,ptnNone]],	#108
	[[9,5,0,0], 0, "+%d to %s (character class Only)", [ptnRaw,ptnSkill,ptnNone,ptnNone]],	#109 ??
	[[8,0,0,0], 20, "Poison Length Reduced by %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#110
	[[9,0,0,0], 20, "Damage +%d", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#111
	[[7,0,0,0], -1, "Hit Causes Monster to Flee %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Hit Blinds Target +%d", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% Damage Taken Goes to Mana", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[1,0,0,0], 0, "Ignore Target Defense", [ptnNone,ptnNone,ptnNone,ptnNone]],	#115
	[[7,0,0,0], 0, "%d%% Target Defense", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Prevent Monster Heal", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[1,0,0,0], 0, "Half Freeze Duration", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 20, "%d%% to Attack Rating", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#119
	[[7,0,0,0], 128, "%d to Monster Defense Per Hit", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 20, "+%d%% Damage to Demons", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[9,0,0,0], 20, "+%d%% Damage to Undead", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[10,0,0,0], 128, "+%d to Attack Rating against Demons", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#123
	[[10,0,0,0], 128, "+%d to Attack Rating against Undead", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#124
	[[1,0,0,0], 0, "Throwable", [ptnNone,ptnNone,ptnNone,ptnNone]],	#125
	[[3,3,0,0], 0, "%+d to %s Skills", [ptnRaw,ptnSkillTree,ptnNone,ptnNone]],	#126
	[[3,0,0,0], 0, "+%d to All Skill Levels", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "Attacker Takes Lightning Damage of %d", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#128
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "Freezes Target %d", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#134
	[[7,0,0,0], 0, "%d%% Chance of Open Wounds", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d%% Chance of Crushing Blow", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "+%d Kick Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "+%d to Mana After Each Kill", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#138
	[[7,0,0,0], 0, "+%d Life after each Demon Kill", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d%% Extra Bloody", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#140
	[[7,0,0,0], 0, "%d%% Deadly Strike", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Fire Absorb %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#142
	[[7,0,0,0], 0, "%d Fire Absorb", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Lightning Absorb %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d Lightning Absorb", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Magic Absorb %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d Magic Absorb", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Cold Absorb %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "%d Cold Absorb", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "Slows Target by %d%%", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#150
	[[9,5,0,0], 0, "Add %s Aura (Level %d) When Equipped", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#151
	[[1,0,0,0], 0, "Indestructible", [ptnNone,ptnNone,ptnNone,ptnNone]],	#152
	[[1,0,0,0], 0, "Cannot Be Frozen", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 20, "%d%% Slower Stamina Drain", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[10,7,0,0], 0, "%d%% Reanimate As: %d", [ptnRaw,ptnRaw,ptnNone,ptnNone]],	#155, monster id
	[[7,0,0,0], 0, "Piercing Attack (%d)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#156
	[[7,0,0,0], 0, "Fires Magic Arrows (%d)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#157
	[[7,0,0,0], 0, "Fires Explosive Arrows or Bolts (%d)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Minimum Throw Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[7,0,0,0], 0, "+%d to Maximum Throw Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#160
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	#seems there are no 179~187 in 1.10!!!
	[[3,0,0,0], 0, "+%d to Druid Skill Levels", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#179
	[[3,0,0,0], 0, "+%d to Assassin Skill Levels", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#180
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#181
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#182
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#183
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#184
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#185
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#186
	[[9,5,0,0], 0, "%s +%d (character class Only)", [ptnSkill,ptnRaw,ptnNone,ptnNone]],	#187
	[[16,3,0,0], 0, "%s Skills set +%d (character class Only)", [ptnRaw,ptnRaw,ptnNone,ptnNone]],	#188
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[4,0,0,0], 0, "Adds %d extra sockets to the item.", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#194
	[[6,10,7,0], 0, "cast %s (level %d, %d%% Chance) on attack", [ptnSkill,ptnRaw,ptnRaw,ptnNone]],	#195
	[[6,10,7,0], 0, "cast %s (level %d, %d%% Chance) on kill", [ptnSkill,ptnRaw,ptnRaw,ptnNone]],	#196
	[[6,10,7,0], 0, "cast %s (level %d, %d%% Chance) on death", [ptnSkill,ptnRaw,ptnRaw,ptnNone]],	#197
	[[6,10,7,0], 0, "cast %s (level %d, %d%% Chance) on striking", [ptnSkill,ptnRaw,ptnRaw,ptnNone]],#198
	[[6,10,7,0], 0, "cast %s (level %d, %d%% Chance) on level up", [ptnSkill,ptnRaw,ptnRaw,ptnNone]],#199
	[[6,10,7,0], 0, "+%d%% Chance to cast level %d %s on striking", [ptnRaw,ptnRaw,ptnSkill,ptnNone]],#200 ??
	[[6,10,7,0], 0, "cast %s (level %d, %d%% Chance) when struck", [ptnSkill,ptnRaw,ptnRaw,ptnNone]],#201
	[[9,5,7,0], 0, "+%d%% Chance to cast level %d %s when struck", [ptnRaw,ptnRaw,ptnSkill,ptnNone]],#??
	[[9,5,7,0], 0, "+%d%% Chance to cast level %d %s when struck", [ptnRaw,ptnRaw,ptnSkill,ptnNone]],#203 ??
	[[6,10,8,8], 0, "%s (level %d, %d/%d Charges)", [ptnSkill,ptnRaw,ptnRaw,ptnRaw]],	#204
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],	#213
	[[6,0,0,0], 0, "+%d to Defense (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#214
	[[6,0,0,0], 0, "%d%% Enhanced Defense (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Life (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Mana (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Maximum Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% Enhanced Maximum Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Strength (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#220
	[[6,0,0,0], 0, "+%d to Dexterity (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Energy (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Vitality (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d to Attack Rating (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% Bonus to Attack Rating (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d Cold Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#226
	[[6,0,0,0], 0, "+%d Fire Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d Lightning Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d Poison Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Cold Resist +%d%% (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#230
	[[6,0,0,0], 0, "Fire Resist +%d%% (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Lightning Resist +%d%% (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Poison Resist +%d%% (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d%% Cold Absorb (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#234
	[[6,0,0,0], 0, "+%d%% Fire Absorb (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d%% Lightning Absorb (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d%% Poison Absorb (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[5,0,0,0], 0, "Attacker Takes Damage of %d (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#238
	[[6,0,0,0], 0, "%d%% Extra Gold from Monsters (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#239
	[[6,0,0,0], 0, "%d%% Better Chance of Getting Magic Items (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Heal Stamina Plus %d%% (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Stamina +%d (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#242
	[[6,0,0,0], 0, "%d%% Damage to Demons (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#243
	[[6,0,0,0], 0, "%d%% Damage to Undead (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d%% to Attack Rating against Demons (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d%% to Attack Rating against Undead (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% Chance of Crushing Blow (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% Chance of Open Wounds (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "+%d% Kick Damage (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "%d%% to Deadly Strike (Based on Character Level)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#250
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[6,0,0,0], 0, "Repairs 1 durability in %d seconds", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#252
	[[6,0,0,0], 0, "Replenishes Quantity (1 in %d seconds)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#??
	[[8,0,0,0], 0, "Increased Stack Size (%d)", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#254
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],	#255
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],	#267
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Defense", [ptnTime,ptnRaw,ptnRaw,ptnNone]],	#268
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Enhanced Defense", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Life", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Mana", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Enhanced Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Strength", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Dexterity", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Energy", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Vitality", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Enhanced Attack Rating", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Attack Rating", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Cold Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Fire Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Lightning Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Poison Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Cold Resist", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Fire Resist", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Lightning Resist", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Poison Resist", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Cold Absorb", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Fire Absorb", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Lightning Absorb", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Poison Absorb", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Extra Gold from Monsters", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Better Chance of Getting Magic Items", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) Heal Stamina Plus %d%%-%d%%", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Stamina", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Damage to Demons", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Damage to Undead", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Attack Rating against Demons", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d to Attack Rating against Undead", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Chance of Crushing Blow", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Chance of Open Wounds", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) +%d-%d Kick Damage", [ptnTime,ptnRaw,ptnRaw,ptnNone]],
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Deadly Strike", [ptnTime,ptnRaw,ptnRaw,ptnNone]],	#303
	[[2,10,10,0], 0, "(Increases %s) %d%%-%d%% Gem Find", [ptnTime,ptnRaw,ptnRaw,ptnNone]],	#304
	[[8,0,0,0], 50, "%d%% to Enemy Cold Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#305
	[[8,0,0,0], 50, "%d%% to Enemy Fire Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#306
	[[8,0,0,0], 50, "%d%% to Enemy Lightning Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#307
	[[8,0,0,0], 50, "%d%% to Enemy Poison Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#308
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],	#310
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],	#320
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],
	[[0,0,0,0], 0, "N/A", [ptnNone,ptnNone,ptnNone,ptnNone]],	#328
	[[9,0,0,0], 50, "+%d to Fire Skill Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#329
	[[9,0,0,0], 50, "+%d to Lightning Skill Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#330
	[[9,0,0,0], 50, "+%d to Cold Skill Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#331
	[[9,0,0,0], 50, "+%d to Poison Skill Damage", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#332
	[[8,0,0,0], 0, "%d%% to Enemy Cold Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#333
	[[8,0,0,0], 0, "%d%% to Enemy Fire Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#334
	[[8,0,0,0], 0, "%d%% to Enemy Lightning Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#335
	[[8,0,0,0], 0, "%d%% to Enemy Poison Resistance", [ptnRaw,ptnNone,ptnNone,ptnNone]],	#336
]

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
		#93, #%d%% Increased Attack Speed
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
			stream.append(self._props[id][0], arrPropTbl[id][0][0])
			stream.append(self._props[id][1], arrPropTbl[id][0][1])
			stream.append(self._props[id][2], arrPropTbl[id][0][2])
			stream.append(self._props[id][3], arrPropTbl[id][0][3])

		for v in self._nonClassSkills:
			stream.append(97, 9)
			stream.append(v[0], arrPropTbl[97][0][0])
			stream.append(v[1], arrPropTbl[97][0][1])
			stream.append(v[2], arrPropTbl[97][0][2])
			stream.append(v[3], arrPropTbl[97][0][3])

		for id in sorted(self._all_resistance):
			stream.append(id, 9)
			stream.append(0xff, 8)

		stream.append(0x1ff, 9)

