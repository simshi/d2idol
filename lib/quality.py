Low = 1
Normal = 2
High = 3
Magic = 4
PartOfSet = 5
Rare = 6
Unique = 7
Crafted = 8

byName = {
	"Low": 1,
	"Normal": 2,
	"High": 3,
	"Magic": 4,
	"PartOfSet": 5,
	"Rare": 6,
	"Unique": 7,
	"Crafted": 8,
}

byId = map(lambda t:t[0], sorted(byName.items(), key=lambda t:t[1]))
byId.insert(0, "ERR_QUALITY")
