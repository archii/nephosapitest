# raxapitest

## Intro
A demonstration using DevOps/CICD with the Rackspace APIs to stand up a simple web app reference stack.

To use/Quickstart:

* install the python-heatclient Python package: 'pip install python-heatclient'
* setup your Heat API ENV variables via .bashrc
* run 'make' for a basic example
* run the 'test_heat.sh' script with command line args for stack/host name, Heat template, image name

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
1. Build a customized server using Heat and user-data
2. - [ ] Automate the build using shell scripts, Heat CLI and Make
- [ ] Create a Jenkins job to automatically build/test the project
4. Build the Nginx/PHP-FHM server using Heat and user data
5. Configure automated deployment of a simple PHP app to the web server instance
6. Build out the rest of the infrastructure using Heat (LB, Varnish, DB, Memcache)
7. Web interface for kicking off the build with parameters for build time customization
8. Replacing the user-data hackery with Chef code
9. Replacing the shell scripts and Heat CLI with Python code using the Heat Python API and Pyrax
10. Profit :-)
