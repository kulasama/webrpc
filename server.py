#!/usr/bin/env python
# encoding: utf-8
"""
tests.py

Created by kula on 2010-09-19.
Copyright (c) 2010 __MyCompanyName__. All rights reserved.
"""
                                  
from webrpc import run, rpcserver,get   
 

@rpcserver()
def add(x,y):
    return x+y  
    



    




if __name__ == '__main__':
	run(reloader=True)

