all: test

test: test_heatclient

clean: 
	find . -name "*.pyc" -type f -print -delete

test_heat:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/templates/ponytest_stack.yml

test_heatclient:
	cd heat/heatclient-test && \
	time python ./test.py

test_heatclient_tcserious:
	cd heat/heatclient-test && \
	./test.py -t ../templates/ponytest_stack.yml -i tcserious_image-2014043014

test_heat2:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/templates/ponytest_stack.yml tcserious_image-2014043014

jenkins3:
	time heat stack-create jenkins3.stack -f heat/templates/jenkins.stack.yml -P "myhostname=jenkins3"

chefclient:
	bash test_heat_chef.sh

npf4:
	bash -x test_heat_chef.sh nginx-php-fpm

