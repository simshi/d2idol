# disable all default rules
.SUFFIXES:
MAKEFLAGS+=-r

.PHONY: all test
.DEFAULT: all

all: test

.PHONY: clean
clean:
	@find output/ -name '*.d2i' -exec rm {} \;

test:
	python3 -m unittest discover

