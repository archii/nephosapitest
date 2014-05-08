#!/bin/env python
# coding: utf-8
import os
import ConfigParser
from heatstack import HeatStack
config = ConfigParser.ConfigParser()
config.readfp(open('defaults.cfg'))

import uuid
mystackname = "h" + str(uuid.uuid4().time_mid)
mytemplatefile='7424uu_stack.yml'
#myimagename="Fedora 20 (Heisenbug) (PVHVM)"
myimagename="Red Hat Enterprise Linux 6.5"
mystack = HeatStack(config, mystackname, template_file=mytemplatefile, parameters={"myimagename":myimagename})
daStack = mystack.create()
print "The stack id:", daStack['stack']['id']
blah = 0
