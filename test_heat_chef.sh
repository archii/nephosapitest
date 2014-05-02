#!/bin/bash -x

MYROLE=$1

if [[ -z ${MYROLE} ]]; then 
    #MYROLE='nginx-php-fpm'
    MYROLE='chef-client'
fi

MYJSON="https://d2f8b2f2ed0164ad2acb-f495505e179839f6b036fbd12d4c94d6.ssl.cf4.rackcdn.com/${MYROLE}.json"
MYNAME=`/usr/bin/uuidgen -r | /usr/bin/cut -d- -f2`
heat stack-create -f heat/templates/chef_client_stack.yml stack.${MYNAME} -P "myhostname=hx${MYNAME};myimagename=tcserious_image-2014043014;myadminpass=passwd00;mychefattrib=${MYJSON}"

