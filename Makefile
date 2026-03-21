# disable all default rules
.SUFFIXES:
MAKEFLAGS+=-r

.PHONY: all tests clean
.DEFAULT: all

all: tests

clean:
	@find output/ -name '*.d2i' -exec rm {} \;

tests:
	python3 -m unittest discover

.PHONY: examples
examples:
	@echo "Generating charm items..."
	cd examples && /c/apps/Git/mingw64/bin/python test_charm.py && cd ..
	@echo "Generating unique items..."
	cd examples && /c/apps/Git/mingw64/bin/python test_uniqitem.py && cd ..
	@echo "Generating high quality items..."
	cd examples && /c/apps/Git/mingw64/bin/python test_highquality_tem.py && cd ..
	@echo "Generating set items..."
	cd examples && /c/apps/Git/mingw64/bin/python test_setitem.py && cd ..
	cd examples && /c/apps/Git/mingw64/bin/python test_set_aldurs.py && cd ..
	cd examples && /c/apps/Git/mingw64/bin/python test_set_sigon.py && cd ..
	@echo "All items generated successfully!"
