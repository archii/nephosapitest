MYNAME=`/usr/bin/uuidgen -r | /usr/bin/cut -d- -f2`
heat stack-create -f heat/templates/chef_client_stack.yml stack.${MYNAME} -P "myhostname=hx${MYNAME};myimagename=tcserious_image-2014043014;myadminpass=passwd00"

