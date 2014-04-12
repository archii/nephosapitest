all: test

test: test_heat

test_heat:
	bash test_heat.sh `uuidgen -r | cut -d- -f2`
