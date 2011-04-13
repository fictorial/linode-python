#!/usr/bin/python

import api, os, json, sys

linode = api.Api(os.getenv('LINODE_API_KEY'))
linode_id = os.getenv('LINODE_ID')

try:
  linode.linode_ip_addprivate(LinodeID=linode_id)
except:
  pass

for ip in linode.linode_ip_list(LinodeID=linode_id):
    if not ip.get('ISPUBLIC'):
        print ip.get('IPADDRESS')
        sys.exit(0)
