#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = True                #True and False
print('x is {}'.format(x))
print(type(x))

x = 20 > 19             #comparison operator has return  True or False in the bool type.
print('x is {}'.format(x))
print(type(x))

x = None                #represent the absence of a value.
print('x is {}'.format(x))
print(type(x))


#represent False --> 1.empty string('') 2.Nonetype 3.number 0
#represent True --> 1.anyobject string 2.any number
if x:
    print('True')
else:
    print('False')