# coding: utf-8
import pyrax
#import keyring

pyrax.set_credential_file("/home/admin/pyrax_credentials")
#pyrax.set_credentials("boblabla", "01234567890abcdef")

cs_syd = pyrax.connect_to_cloudservers(region="SYD")
booma = cs_syd.servers.list()

print booma
