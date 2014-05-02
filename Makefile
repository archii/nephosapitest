all: test

test: test_heat

test_heat:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/templates/ponytest_stack.yml

test_heat2:
	time bash test_heat.sh `uuidgen -r | cut -d- -f2` heat/templates/ponytest_stack.yml tcserious_image-20140429

jenkins3:
	time heat stack-create jenkins3.stack -f heat/templates/jenkins.stack.yml -P "myhostname=jenkins3"

npf3:
	time heat stack-create npf3.stack -f heat/templates/chef_client_stack.yml -P "myhostname=npf3;myimagename=tcserious_image-20140429;mychefattrib=https://d2f8b2f2ed0164ad2acb-f495505e179839f6b036fbd12d4c94d6.ssl.cf4.rackcdn.com/nginx-php-fpm.json"

chefclient:
	bash test_heat_chef.sh
