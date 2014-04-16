all: test

test: test_heat

test_heat:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/ponytest_stack.yml

test_heat2:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/ponytest_stack.yml eggs687-201404130220

jenkins3:
	time heat stack-create jenkins3.stack -f heat/jenkins.stack.yml -P "myhostname=jenkins3;myimagename=eggs687-201404130220"
