#!/usr/bin/env python
# coding: utf-8
import os
from time import sleep
import ConfigParser
from heatstack import HeatStack
config = ConfigParser.ConfigParser()
config.readfp(open('defaults.cfg'))

CREATE_POLL_INTERVAL=60
DELETE_POLL_INTERVAL=10
SUTD=True

import uuid
mystackname = "h" + str(uuid.uuid4().time_mid)
mytemplatefile='7424uu_stack.yml'
#myimagename="Fedora 20 (Heisenbug) (PVHVM)"
myimagename="Red Hat Enterprise Linux 6.5"
mystack = HeatStack(config, mystackname, template_file=mytemplatefile, parameters={"myimagename":myimagename})
mystack.id = None
mystack.create()

if mystack.id:
    print "The stack id:", mystack.id
    print "The stack name:", mystack.name
    print "The stack status:", mystack.status()
    while mystack.status() == "CREATE_IN_PROGRESS":
        print "Polling for status in" + str(CREATE_POLL_INTERVAL) + " seconds ..."
        sleep(CREATE_POLL_INTERVAL)
        print mystack.status()
    if (mystack.status() == "CREATE_COMPLETE") and (SUTD):
        print mystack.status()
        sleep(30)
        print "Tearing down stack " + mystack.name + " after successful test..."
        mystack.delete(mystack.id)
        while mystack.status() == "DELETE_IN_PROGRESS":
            print "Polling for DELETE status in " + DELETE_POLL_INTERVAL + " seconds..."
            sleep(DELETE_POLL_INTERVAL)
            print mystack.status()
        if not mystack.status():
            print "Stack " + mystack.name + " is DELETED!"
            print "Test complete!"
    elif (mystack.status() == "CREATE_COMPLETE") and (not SUTD):
        print "Stack " + mystack.name + " is up and running."

blah = 0
