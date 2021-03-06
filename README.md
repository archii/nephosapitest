# raxapitest

## Intro
A demonstration using DevOps/CICD with the Rackspace APIs to stand up a simple web app reference stack.

## Quickstart:
* install the python-heatclient Python package: 'pip install python-heatclient'
* setup your Heat API ENV variables via .bashrc
* run 'make' for a basic example
* read Makefile for examples/tests
* run 'heat/heatclient-test/test.py -h' for list of available commandline parameters

## Notes
Unattended chef-client bootstrap install doc: 
http://docs.opscode.com/install_bootstrap.html#unattended-installs

## Goals
* A demonstrative example of a simple web application stack.  (Load balanced web servers fronted by Varnish and running Nginx/PHP, backend Mysql DB, Memcache and Cloud Files).  
* The example stack will be spawned via basic web form user input for customization (branding, region, flavor, ssh keys, passwords, disk sizing etc.).

## Tools
* Heat Orchestration Template(s)
* Chef
* Jenkins CI
* Github
* PHP, Python, Bash
* Glue and Duct Tape

## Milestones
- [x] Build a customized server using Heat and user-data
- [x] Automate the build using shell scripts, Heat CLI and Make
- [x] Create a Jenkins job to automatically build/test the project
- [ ] ~~Build the Nginx/PHP-FHM server using Heat and user data~~
- [x] Replace the user-data hackery with Chef bootstrapping
- [ ] Automate provisioning of the application infrastructure layer with Chef
- [ ] Configure automated deployment of a simple PHP app to the web server instance
- [ ] Build out the rest of the infrastructure using Heat (LB, Varnish, DB, Memcache)
- [ ] Web interface for kicking off the build with parameters for build time customization
- [x] Replacing the shell scripts and Heat CLI with Python code using the Heat Python API
- [ ] Profit :-)
