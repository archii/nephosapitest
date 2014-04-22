yum -y -v install \
nginx \
php \
php-fpm \
php-devel \
php-common \
php-gd \
php-snmp \
php-cli \
php-pspell \
php-xmlrpc \
php-pear \
php-mcrypt \
;

#php-pecl-memcache
#php-pecl-imagick
#php-pecl-ssh2

adduser -r -M nginx;

cd /etc/nginx && tar -czf ~/NGINX_Config.tar.gz nginx.conf fastcgi_params 