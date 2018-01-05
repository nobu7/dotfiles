#!/usr/bin/env python3

import os
import re


schema       = 'https'
authority    = 'api.digitalocean.com'
path         = '/v2/droplets'
endpoint     = '{schema}://{authority}{path}' \
				 .format(schema=schema, \
						authority= authority,\
						path=path)

data    = 'sata'
token   = 'smoken'

#FIXME format the following string
create_droplet_command = "curl -x POST -d \'{data}\'    					\
                            -H \"Authentication: Bearer {token}\"   		\
                            -H \"Content-type: application/json\"   		\
                            \"{endpoint}\"".format(data=data,               \
                            	token=token,								\
                            	endpoint=endpoint)

print(re.sub(' +','',create_droplet_command))
#os.system(create_droplet_command)
#then we need to wait for the droplet to be created.
#os.system()

#then we need to get the IP address to the droplet that we created(host).
#os.system

#finally we need to clone our dotfiles to the droplet


#os.system('ssh -o "StrictHostKeyChecking no" root@{host}		\
#	\'bash -s\' < dotfiles/run.sh'.format(host=host)')

 