#!/usr/bin/env python

import boto.cloudformation
import sys
import json

conn = boto.cloudformation.connect_to_region('us-east-1')
try:
  for p in conn.describe_stacks(sys.argv[1])[0].parameters:
    if p.key == 'UserData':
      print p.value

except:
  True
