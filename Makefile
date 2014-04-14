all: test

test: test_heat

test_heat:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/ponytest_stack.yml
