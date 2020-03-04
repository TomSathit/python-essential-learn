#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# x = [1, 2, 3, 4, 5, 6]
# x = (1, 2, 3, 4, 5, 6)
# x = range(6)        #--> three parameter in range (start,stop,step) --> range is immutable
# x = list(range(6))  #--> construct a list to mutable.
# x = {'zero': 0, 'one': 1, 'two': 2}  #--> mutable change value pass key


x = [1, 2, 3, 4, 5, 6]          #mutable sequence with list
x[2] = 9                        #mutable can change or add value
print('x is {}'.format(x))
print(type(x))

for i in x:  #for loop sequencing through the list and the each item of list assigns i the value of the item
    print('x is {}'.format(i))

x = {'zero': 0, 'one': 1, 'two': 2}
for i,k in x.items():               #get keys and value from dictionary
    print('{} is {}'.format(i,k))