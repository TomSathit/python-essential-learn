#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7                       #int
print('x is {}'.format(x))
print(type(x))

x = 7.7                     #float
print('x is {}'.format(x))
print(type(x))

x = 14/7                    # new in python3 int / int = float --> different in python2 that get int
print('x is {}'.format(x))
print(type(x))

'''This is the difference between accuracy and precision. 
Because of the way that the computers do floating point, 
they're sacrificing accuracy for precision and so it may do this arithmetic correctly to 17 decimal places,
 which is the precision of the floating point processor inside the computer. 
 But it is not accurate. Accuracy is the true value of a calculation.'''
x = .1 + .1 + .1 - .3       # expect equal to 0  --> no !!!! This is diference between accuracy and precision.
print('x is {}'.format(x))
print(type(x))

from decimal import *       #How to fix that
a = Decimal('.10')
b = Decimal('.3')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))