yum -y -v install java-1.8.0-openjdk-headless.x86_64 git wget;
pip install python-heatclient;
wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat-stable/jenkins.repo && \
  rpm --import http://pkg.jenkins-ci.org/redhat-stable/jenkins-ci.org.key && \
  yum -y -v install jenkins && \
  systemctl start jenkins && \
  systemctl status jenkins && \
  systemctl enable jenkins;