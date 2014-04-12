all: test

test: test_heat

test_heat:
	bash -x test_heat.sh `uuidgen -r | cut -d- -f1`
