#!/usr/bin/env python
# encoding: utf-8
"""
client.py

Created by kula on 2010-09-27.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
from webrpc import rpcclient              

add = rpcclient('add','http://127.0.0.1:8080')

if __name__ == '__main__':
	print add(1,2)

