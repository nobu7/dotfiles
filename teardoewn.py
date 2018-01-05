#!/usr/bin/env python3

import os
import re

token        = 'smoken'
tag          = 'test'
schema       = 'https'
authority    = 'api.digitalocean.com'
path         = '/v2/droplets'
query_string = '?tag_name={tag}'.format(tag=tag)
endpoint     = '{schema}://{authority}{path}{query_string}' \
                 .format(schema=schema, \
                        authority= authority,\
                        path=path,\
                        query_string=query_string)


teardown_droplet_command = "curl -X DELETE                                  \
                            -H \"Content-type: application/json\"           \
                            -H \"Authorization: Bearer {token}\"            \
                            \"{endpoint}\"".format(token=token,             \
                                endpoint=endpoint)
teardown_droplet_command=re.sub(' +',' ',teardown_droplet_command)
print(teardown_droplet_command)