#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
x = "Hello Mars"                # double quotes & single quotes are not difference
print('x is {}'.format(x))

x =  """

I'm from
Altotech
team
"""                            #multi-line string can do with single quotes too (''' ''')
print('x is {}'.format(x))

x = 'one {} {}'.format(2,3)     #strings are objects even literal strings so we can run methods on that object.
print('x is {}'.format(x))      #--> add more method

x = 'one {1} {0}'.format(2,3)           #change order
print('x is {}'.format(x))

x = 'one {1:<7} {0:>7}'.format(2,3)     #spacce left and right
print('x is {}'.format(x))

x = 'one "{1:<07}" "{0:>07}"'.format(2,3)   #spacce left and right with "" in ''
print('x is {}'.format(x))                #add 0 between spaces

y = 2020
z = 2021
x = f'2019 {y:<9} {z:>8}'             # fstrings are available in python 3.6 and after.
print('x is {}'.format(x))      # fstring use the format method on the string class

print(type(x))
