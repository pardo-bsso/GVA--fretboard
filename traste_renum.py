#!/usr/bin/python

import sys

sch = open(sys.argv[1]).readlines()

idx = 0;
out = []

for l in sch:
    if 'traste%i' in l:
        out.append(l.replace('%i', '%02i:1' % idx))
        idx += 1
    else:
        out.append(l)

open('out'+sys.argv[1], 'wb').write(''.join(out))
