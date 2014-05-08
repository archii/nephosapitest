from keystoneclient.v2_0 import client as ksclient
from heatclient.common import utils

class KSClient():
    def __init__(self, config):
        self.tenant_id = config.get('auth','tenant_id') or utils.env('OS_TENANT_ID')
        self.tenant_name = config.get('auth','tenant_name') or utils.env('OS_TENANT_NAME')
        self.password = config.get('auth', 'password') or utils.env('OS_PASSWORD')
        self.username = config.get('auth', 'username') or utils.env('OS_USERNAME')
        self.auth_url = config.get('auth', 'auth_url') or utils.env('OS_AUTH_URL')
        self.auth_token = config.get('auth', 'auth_token') or utils.env('OS_AUTH_TOKEN')
        self.heat_url = config.get('heat', 'heat_url') or utils.env('HEAT_URL')
        self.service_type = config.get('auth', 'service_type') or utils.env('OS_SERVICE_TYPE')
        self.endpoint_type = config.get('auth', 'endpoint_type') or utils.env('OS_ENDPOINT_TYPE')
        self.include_pass = config.get('heat', 'include_pass') or bool(utils.env('HEAT_INCLUDE_PASSWORD'))
    
    def get(self, **kwargs):
        """Get an endpoint and auth token from Keystone.

        :param username: name of user
        :param password: user's password
        :param tenant_id: unique identifier of tenant
        :param tenant_name: name of tenant
        :param auth_url: endpoint to authenticate against
        :param token: token to use instead of username/password
        """

        kwargs = {
            'username': self.username,
            'password': self.password,
            'token': self.auth_token,
            'tenant_id': self.tenant_id,
            'tenant_name': self.tenant_name,
            'auth_url': self.auth_url,
            'service_type': self.service_type,
            'endpoint_type': self.endpoint_type,
            'insecure': False,
            'include_pass': self.include_pass
        }

        kc_args = {'auth_url': kwargs.get('auth_url'),
                   'insecure': kwargs.get('insecure')}

        if kwargs.get('tenant_id'):
            kc_args['tenant_id'] = kwargs.get('tenant_id')
        else:
            kc_args['tenant_name'] = kwargs.get('tenant_name')

        if kwargs.get('token'):
            kc_args['token'] = kwargs.get('token')
        else:
            kc_args['username'] = kwargs.get('username')
            kc_args['password'] = kwargs.get('password')

        return ksclient.Client(**kc_args)

# kwargs = {
#     'username': args.os_username,
#     'password': args.os_password,
#     'token': args.os_auth_token,
#     'tenant_id': args.os_tenant_id,
#     'tenant_name': args.os_tenant_name,
#     'auth_url': args.os_auth_url,
#     'service_type': args.os_service_type,
#     'endpoint_type': args.os_endpoint_type,
#     'insecure': args.insecure,
#     'include_pass': args.include_password
# }
# 
# endpoint = args.heat_url
# 
# if not args.os_no_client_auth:
#     _ksclient = self.get_ksclient(**kwargs)
#     token = args.os_auth_token or _ksclient.auth_token
# 
#     kwargs = {
#         'token': token,
#         'insecure': args.insecure,
#         'ca_file': args.ca_file,
#         'cert_file': args.cert_file,
#         'key_file': args.key_file,
#         'username': args.os_username,
#         'password': args.os_password,
#         'endpoint_type': args.os_endpoint_type,
#         'include_pass': args.include_password
#     }
# 
#     if args.os_region_name:
#         kwargs['region_name'] = args.os_region_name
# 
#     if not endpoint:
#         endpoint = self._get_endpoint(_ksclient, **kwargs)
# 
# if args.api_timeout:
#     kwargs['timeout'] = args.api_timeout
# 
# client = heat_client.Client(api_version, endpoint, **kwargs)
# 
# args.func(client, args)
