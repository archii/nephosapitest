#!/usr/bin/env python
# coding: utf-8
import sys
import os
import uuid
from time import sleep
import json
import ConfigParser
from heatstack import HeatStack
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter


config = ConfigParser.ConfigParser()
#config.readfp(open('defaults.cfg'))
config.read(['defaults.cfg', 'heat/heatclient-test/defaults.cfg'])


__all__ = []
__version__ = 0.1
__date__ = '2013-12-09'
__updated__ = '2013-12-09'

DEBUG = 1
TESTRUN = 0
PROFILE = 0

CREATE_POLL_INTERVAL=60
DELETE_POLL_INTERVAL=5
# This is now set via the --sutd command line flag
#SUTD=True

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''
    def __init__(self, msg):
        super(CLIError).__init__(type(self))
        self.msg = "E: %s" % msg
    def __str__(self):
        return self.msg
    def __unicode__(self):
        return self.msg


def generate_stackname():
    return  "x" + "-" + str(uuid.uuid4().time_mid)

def generate_hostname(mystackname):
    return  "h" + "-" + mystackname + "-" + str(uuid.uuid4().time_mid)

def main(argv=None): 
    '''main()'''
    
    if argv is None:
        argv = sys.argv
    else:
        sys.argv.extend(argv)

    program_name = os.path.basename(sys.argv[0])
    program_version = "v%s" % __version__
    program_build_date = str(__updated__)
    program_version_message = '%%(prog)s %s (%s)' % (program_version, program_build_date)
    #program_shortdesc = __import__('__main__').__doc__.split("\n")[1]
    program_shortdesc = program_version_message
    program_license = '''%s

  Created by user_name on %s.
  Copyright 2013 organization_name. All rights reserved.
  
  Licensed under the Apache License 2.0
  http://www.apache.org/licenses/LICENSE-2.0
  
  Distributed on an "AS IS" basis without warranties
  or conditions of any kind, either express or implied.

USAGE
''' % (program_shortdesc, str(__date__))

    try:
        # Setup argument parser
        parser = ArgumentParser(description=program_license, formatter_class=RawDescriptionHelpFormatter)
        #parser.add_argument("-r", "--recursive", dest="recurse", action="store_true", help="recurse into subfolders [default: %(default)s]")
        #parser.add_argument("-e", "--exclude", dest="exclude", help="exclude paths matching this regex pattern. [default: %(default)s]", metavar="RE" )
        #parser.add_argument(dest="paths", help="paths to folder(s) with source file(s) [default: %(default)s]", metavar="path", nargs='+')
        parser.add_argument('-V', '--version', action='version', version=program_version_message)
        parser.add_argument("-v", "--verbose", dest="verbose", action="count", help="set verbosity level [default: %(default)s]")
        #parser.add_argument("-i", "--image", dest="image", default="Red Hat Enterprise Linux 6.5", help="name of bootstrap image to use [default: %(default)s]")
        parser.add_argument("-i", "--image", dest="image", default=None, help="name of bootstrap image to use [default: %(default)s]")
        parser.add_argument("-t", "--template", dest="templatefile", default=None, help="name of bootstrap image to use [default: %(default)s]")
        parser.add_argument("--sutd", dest="sutd", action="store_true", help="whether or not to perform the setup/teardown cycle [default: %(default)s]")
        parser.add_argument("--hostname", dest="hostname", default=None, help="name of server where single server templates are in use [default: %(default)s]")
        parser.add_argument("--stackname", dest="stackname", default=None, help="name of stack [default: %(default)s]")
        parser.add_argument("--role", dest="role", default=None, help="name of (chef) role to assume in single server stacks [default: %(default)s]")
        # the only parameters allowed from the test script at the moment are image, so don't need free from parameters like the heat client cli
        #parser.add_argument("-P", "--parameters", dest="parameters", help="parameters to use as input to the given Heat template [default: %(default)s]")

        # Process arguments
        args = parser.parse_args()
        
        #paths = args.paths
        verbose = args.verbose
        #recurse = args.recurse
        #inpat = args.include
        #expat = args.exclude
        
        if verbose > 0:
            print("Verbose mode on")
#             if recurse:
#                 print("Recursive mode on")
#             else:
#                 print("Recursive mode off")
#         
#         if inpat and expat and inpat == expat:
#             raise CLIError("include and exclude pattern are equal! Nothing will be processed.")
#         
#         for inpath in paths:
#             ### do something with inpath ###
#             print(inpath)
#         return 0
    except KeyboardInterrupt:
        ### handle keyboard interrupt ###
        return 0
    except Exception, e:
        if DEBUG or TESTRUN:
            raise(e)
        indent = len(program_name) * " "
        sys.stderr.write(program_name + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help")
        return 2
    
    if not args.stackname:
        mystackname = generate_stackname()
    else:
        mystackname = args.stackname
        
    if args.hostname:
        myhostname = args.hostname
    else:
        myhostname = None

    if args.role:
        myjson="https://d2f8b2f2ed0164ad2acb-f495505e179839f6b036fbd12d4c94d6.ssl.cf4.rackcdn.com/%s.json" % (args.role)
    else:
        myjson=None
        
    if args.sutd:
	SUTD=True
        args.templatefile='../templates/7424uu_stack.yml'
    else:
        SUTD=False

    if args.templatefile:
        mytemplatefile=args.templatefile
    else:
        parser.print_help()
	print
        print "'--template' argument is REQUIRED."
        sys.exit()

    #myimagename="Fedora 20 (Heisenbug) (PVHVM)"
    myimagename=args.image
    #mystack = HeatStack(config, mystackname, template_file=mytemplatefile, parameters={"myimagename":myimagename,"myhostname":myhostname})
    mystack = HeatStack(config, mystackname, template_file=mytemplatefile)
    mystack.parameters = {}
    if myhostname:
        mystack.parameters = {"myhostname":myhostname}
    if myimagename:
        mystack.parameters = {"myimagename":myimagename}
    if myjson:
        mystack.parameters["mychefattrib"] = myjson
    
    
    # the only parameters allowed from the test script at the moment are image, so don't need free from parameters like the heat client cli
    #mystack.parameters = args.parameters
    mystack.id = None
    mystack.create()
    
    if mystack.id:
        print "The stack id:", mystack.id
        print "The stack name:", mystack.name
        print "The stack status:", mystack.status()
        while mystack.status() == "CREATE_IN_PROGRESS":
            print "Polling for status in " + str(CREATE_POLL_INTERVAL) + " seconds ..."
            sleep(CREATE_POLL_INTERVAL)
            print mystack.status()
    
        if (mystack.status() == "CREATE_COMPLETE") and (SUTD):
            print mystack.status()
            print json.dumps(mystack.summary(), sort_keys=True, indent=4, separators=(',', ': '))
            print "Tearing down stack " + mystack.name + " after successful test..."
            sleep(10)
            mystack.delete()
            print mystack.status()
            print json.dumps(mystack.summary(), sort_keys=True, indent=4, separators=(',', ': '))
            sleep(5)
            while mystack.status() == "DELETE_IN_PROGRESS":
                print "Polling for DELETE status in " + str(DELETE_POLL_INTERVAL) + " seconds..."
                sleep(DELETE_POLL_INTERVAL)
                print mystack.status()
            if not mystack.status():
                print "Stack " + mystack.name + " is DELETED!"
                print "Test complete!"
        elif (mystack.status() == "CREATE_COMPLETE") and (not SUTD):
            print "Stack " + mystack.name + " is up and running."
    

if __name__ == "__main__":
    if DEBUG:
        #sys.argv.append("-h")
        sys.argv.append("-v")
        #sys.argv.append("-r")
    if TESTRUN:
        import doctest
        doctest.testmod()
    if PROFILE:
        import cProfile
        import pstats
        profile_filename = 'hilo.cli_profile.txt'
        cProfile.run('main()', profile_filename)
        statsfile = open("profile_stats.txt", "wb")
        p = pstats.Stats(profile_filename, stream=statsfile)
        stats = p.strip_dirs().sort_stats('cumulative')
        stats.print_stats()
        statsfile.close()
        sys.exit(0)
    sys.exit(main())
