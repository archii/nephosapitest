import os
import ConfigParser
import logging

import heatclient
from heatclient import client as heat_client
from heatclient.common import utils
from heatclient.common import template_utils
from heatclient import exc
from heatclient.openstack.common import strutils

from auth import KSClient

logger = logging.getLogger(__name__)

class HeatStack():
    #def __init__(self, config, stackname, stacktype='default', template_file=None, template_url=None, parameters = None):
    def __init__(self, config, stackname, stacktype='default', template_file=None, template_url=None):
        self.tenant_id = ( config.get('auth','tenant_id') or utils.env('OS_TENANT_ID') )
        self.tenant_name = ( config.get('auth','tenant_name') or utils.env('OS_TENANT_NAME') )
        self.password = ( config.get('auth', 'password') or utils.env('OS_PASSWORD') )
        self.username = ( config.get('auth', 'username') or utils.env('OS_USERNAME') )
        self.auth_url = ( config.get('auth', 'auth_url') or utils.env('OS_AUTH_URL') )
        self.heat_url = ( config.get('heat', 'heat_url') or utils.env('HEAT_URL') )
        self.endpoint_type = ( config.get('auth', 'endpoint_type') or utils.env('OS_ENDPOINT_TYPE') )
        self.include_pass = ( config.get('heat', 'include_pass') or bool(utils.env('HEAT_INCLUDE_PASSWORD')) )
        self.region_name = ( config.get('heat', 'region_name') or utils.env('OS_REGION_NAME') )
        self.api_version = ( config.get('heat', 'api_version') or utils.env('HEAT_API_VERSION') )
        self.KSclient = KSClient(config)
        self.ksclient = self.KSclient.get()
        self.token = self.ksclient.auth_token
        self.name = stackname
        self.template_file = ( template_file or config.get('stack', 'template_file') )
        self.template_url = template_url
        self.template_object = None
        self.stacktype = stacktype
        # parameters should be injected into the HeatStack object after the class has been instantiated in an external script
        #self.parameters = parameters
        
        kwargs = {
            'token': self.token,
            'insecure': False,
            'ca_file': None,
            'cert_file': None,
            'key_file': None,
            'username': self.username,
            'password': self.password,
            'endpoint_type': self.endpoint_type,
            'include_pass': self.include_pass,
            'region_name': self.region_name,
            'timeout': None
        }

        self.client = heat_client.Client(self.api_version, self.heat_url, **kwargs)


    def create(self):
        tpl_files, template = template_utils.get_template_contents(
            self.template_file,
            self.template_url,
            self.template_object,
            self.client.http_client.raw_request)
        env_files, env = template_utils.process_environment_and_files()

        fields = {
            'stack_name': self.name,
            'disable_rollback': False, #not(args.enable_rollback),
            'template': template,
            'files': dict(list(tpl_files.items()) + list(env_files.items())),
            'environment': env
        }
        
        if self.parameters:
            fields['parameters'] = self.parameters #utils.format_parameters(self.parameters),
            
        myresult = self.client.stacks.create(**fields)
        self.id = myresult['stack']['id']

    def delete(self):
        return self.client.stacks.delete(self.id)
    
    def status(self):
        return self.client.stacks.get(self.id).stack_status
    
    def summary(self):
        stack = self.client.stacks.get(self.id)
        stack_summary = {
             "id":stack.id, 
             'name':stack.stack_name, 
             'status':stack.stack_status,
             'description':stack.description,
             'creation_time':stack.creation_time
        }
        return stack_summary

#     def get(self):
#         return self.botoconnection.describe_stacks(self.name)[0]
# 
