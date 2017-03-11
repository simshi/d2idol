# disable all default rules
.SUFFIXES:
MAKEFLAGS+=-r

.PHONY: all test
.DEFAULT: all

all: test

test:
	python -m unittest discover

