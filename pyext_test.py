#!/usr/bin/python
from pyext import *
import sys

@overload.args(str)
def x(a):
    print 's', a

@overload.args(int)
def x(a):
    print 'i', a

x(1)
x('s')

n = RuntimeModule.from_string('n', 'class x():\n def y(self): pass')
print n.x.y

with switch('x') as case:
    if case(1): print 2
    elif case('x'): print 0
    else: print 1

for case in switch('x'):
    if case('x'): print 0

@tail_recurse()
def x(s):
    if s == 0: return
    sys.stdout.write('\r')
    sys.stdout.write(str(s))
    x(s-1)
