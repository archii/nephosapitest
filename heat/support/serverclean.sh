cd ~root && rm -f heat-script.* cfn-userdata.log;
cat /dev/null > /var/log/boot.log;
cat /dev/null > /var/log/cloud-init.log;
cat /dev/null > /var/log/cloud-init-output.log;
cat /dev/null > /var/log/cron.log;
cat /dev/null > /var/log/lastlog.log;
cat /dev/null > /var/log/messages;
cat /dev/null > /var/log/nova-agent.log;
cat /dev/null > /var/log/port-handler.log;
cat /dev/null > /var/log/secure.log;
cat /dev/null > /var/log/wtmp;
cat /dev/null > /var/log/yum.log;
rm -rf /var/cache/yum/*;
rm -f /etc/sysconfig/iptables;

export HISTFILESIZE=0;
export HISTSIZE=0;
