#!/usr/bin/env python3
from pyext import *

@overload.args(None)
def x(a:str):
    print(1)

@overload.args(None)
def x(a:int, b:str):
    print(2)

x('a')
x(1, 'b')

with switch('a') as case:
    if case('a'): print(0)
    if case('b'): print(1)

for case in switch('a'):
    if case('a'): print(0)
    if case('b'): print(1)

@tail_recurse()
def add(a, b):
    if a == 0: return b
    return add(a-1, b+1)

print(add(10, 1))
