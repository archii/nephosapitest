# coding: utf-8
#import ipdb
import pyrax

if __name__ == '__main__':
    #ipdb.set_trace()
    
    pyrax.set_credential_file("./pyrax_credentials")
    cs_syd = pyrax.connect_to_cloudservers(region="SYD")
    sydservers = cs_syd.servers.list()
    sydimages = cs_syd.images.list()
    #
    print sydimages[0]
    sydimages[0]
    type(sydimages[0])
    sydimages[0].id
    sydimages[0].name
    sydimages[0].human_id
    cs_syd.list_snapshots()
    cs = cs_syd
    flvs = cs.list_flavors()
    #for flv in flvs:
    #        print "Name:", flv.name
    #        print "  ID:", flv.id
    #        print "  RAM:", flv.ram
    #        print "  Disk:", flv.disk
    #        print "  VCPUs:", flv.vcpus
        
    #server = cs.servers.create("pony46", u'5140b7e1-77a7-4ffb-ad9d-76bb834bd6f9', 2)
    server=sydservers[0]
    server.id
    server.status
    server.networks
    #server.adminPass
    #get_ipython().magic(u'save')
    #get_ipython().magic(u'save booma6712')
    #get_ipython().magic(u'save booma6713 1-24')
    server.status
    server.status
    server.status
    server.progress
    server.human_id
    server.hostId
    server.id
    server.image
    server.get_vnc_console.__doc__
    server.get_vnc_console('novnc')
    server.user_id
    #server.adminPass
    #server.get_password
    #server.get_password()
    #server.delete
    server.delete.__doc__
    #server.delete()
    cs.servers.list()
    cs.list_base_images()
    for i in cs.list_base_images():
        print i.name, i.id
        
    #server = cs.servers.create("pony48", u'6110edfe-8589-4bb1-aa27-385f12242627', 2)
    server.name
    server.id
    server.status
    server.image.values
    server.image.values()
    #server = cs.servers.create("pony50", u'052ce2a1-6038-4834-8228-e377211cf059', 2)
    server.status
    server.id
    cs_syd.servers
    cs_syd.servers.list()
    for i in cs_syd.servers.list():
        print i.name, i.id, i.image
        
    for i in cs_syd.servers.list():
        print i
        
    klist = cs_syd.servers.list()
    klist
    klist[0].id
    klist[0].image
    klist = {}
    for i in cs_syd.servers.list():
        klist[i.name] = i
        
    print klist
    #klist['pony48']
    #klist['pony48'].id
    #klist['pony48'].delete()
    #klist['pony50'].delete()
    #get_ipython().magic(u'save ipython-pyrax1-dump 1-76')