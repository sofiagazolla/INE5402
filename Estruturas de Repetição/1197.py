# -*- coding: utf-8 -*-
while True:
    try:
        v,t = input().split()
        v = int(v)
        t = int(t)
        print ("%d" % ((v*t)*2))
        
    except EOFError:
        break
