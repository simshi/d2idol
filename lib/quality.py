Low = 1
Normal = 2
High = 3
Magic = 4
PartOfSet = 5
Rare = 6
Unique = 7
Crafted = 8

byName = {
	"ERR_QUALITY": 0,
	"Low": 1,
	"Normal": 2,
	"High": 3,
	"Magic": 4,
	"PartOfSet": 5,
	"Rare": 6,
	"Unique": 7,
	"Crafted": 8,
}
byId = [t[0] for t in sorted(byName.items(), key=lambda t:t[1])]
