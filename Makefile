all: test

test: test_heatclient

clean: 
	find . -name "*.pyc" -type f -print -delete

test_heatclient:
	cd heat/heatclient-test && \
	time python ./test.py --sutd

test_heatclient_tcserious:
	cd heat/heatclient-test && \
	time python ./test.py --sutd -t ../templates/ponytest_stack.yml -i tcserious-2014060312

jenkins4:
	cd heat/heatclient-test && \
	time python ./test.py --sutd -t ../templates/jenkins.stack.yml --stackname jenkins4.stack --hostname jenkins4

chefclient:
	cd heat/heatclient-test && \
	./test.py --sutd --template ../templates/chef_client_stack.yml --stackname chef2 --role chef-client --image tcserious-2014060312

npf4:
	cd heat/heatclient-test && \
	./test.py --sutd --template ../templates/chef_client_stack.yml --stackname npf4 --role nginx-php-fpm --image tcserious-2014060312

