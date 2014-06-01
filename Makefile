all: test

test: test_heatclient

clean: 
	find . -name "*.pyc" -type f -print -delete

test_heatclient:
	cd heat/heatclient-test && \
	time python ./test.py

test_heatclient_tcserious:
	cd heat/heatclient-test && \
	time python ./test.py -t ../templates/ponytest_stack.yml -i tcserious_image-2014043014

jenkins4:
	cd heat/heatclient-test && \
	time python ./test.py -t ../templates/jenkins.stack.yml --stackname jenkins4.stack --hostname jenkins4

chefclient:
	#bash test_heat_chef.sh
	cd heat/heatclient-test && \
	./test.py --template ../templates/chef_client_stack.yml --stackname chef2 --role chef-client --image tcserious_image-2014043014

npf4:
	bash -x test_heat_chef.sh nginx-php-fpm

