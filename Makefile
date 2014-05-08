all: test

test: test_heat

test_heat:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/templates/ponytest_stack.yml

test_heat2:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/templates/ponytest_stack.yml tcserious_image-2014043014

jenkins3:
	time heat stack-create jenkins3.stack -f heat/templates/jenkins.stack.yml -P "myhostname=jenkins3"

chefclient:
	bash test_heat_chef.sh

npf4:
	bash -x test_heat_chef.sh nginx-php-fpm

