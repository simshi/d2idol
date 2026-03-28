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
	@echo "Generating [ear] items..."
	@PYTHONPATH=. python3 examples/test_earitem.py
	@echo "Generating [charm] items..."
	@PYTHONPATH=. python3 examples/test_charm.py
	@echo "Generating [unique] items..."
	@PYTHONPATH=. python3 examples/test_uniqitem.py
	@echo "Generating [high quality] items..."
	@PYTHONPATH=. python3 examples/test_highquality_item.py
	@echo "Generating [superior] items..."
	@PYTHONPATH=. python3 examples/test_superior_item.py
	@echo "Generating [set] items..."
	@PYTHONPATH=. python3 examples/test_setitem.py
	@PYTHONPATH=. python3 examples/test_set_aldurs.py
	@PYTHONPATH=. python3 examples/test_set_sigon.py
	@PYTHONPATH=. python3 examples/test_set_natalya.py
	@PYTHONPATH=. python3 examples/test_set_trangouls.py
	@echo "All items generated successfully!"
