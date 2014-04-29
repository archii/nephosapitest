#!/bin/bash
sleep 30;
yum -y -v remove firewalld && \
  yum -y -v install iptables-services && \
  sleep 10 && \
  service iptables restart;
yum -y -v update && \
  systemctl enable iptables.service && \
  exit 0;
