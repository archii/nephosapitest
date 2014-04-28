#!/bin/bash

source /opt/raxapitest/chef_client_bootstrap.env;
echo $PLATFORM;
echo $PLATFORM_VERSION;
echo $MACHINE_ARCH;

sleep 60;

yum -y -v remove firewalld && \
  yum -y -v install iptables-services && \
  sleep 30 && \
  service iptables restart;

systemctl enable iptables.service;

yum -y -v update;

userdel -rf fedora;

#yum install -y -v https://opscode-omnibus-packages.s3.amazonaws.com/el/6/x86_64/chef-11.12.2-1.el6.x86_64.rpm && \
#yum install -y -v http://www.opscode.com/chef/download?p=$PLATFORM&pv=$PLATFORM_VERSION&m=$MACHINE_ARCH&v=latest&prerelease=false&nightlies=false && \
curl -L https://www.opscode.com/chef/install.sh | bash && \
  exit 0
