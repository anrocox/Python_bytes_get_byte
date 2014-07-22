#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

How to get a byte from a bytes object in Python?

¿Cómo obtener un byte de un objeto bytes en Python?
'''

#create a bytes object
b = bytes([104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100])
print(b)

#is similar to the handling of lists, the index is defined in brackets
i = b[4]
print(i)
print(chr(i))

#can also use negative indices to get a byte from bytes object
i = b[-5]
print(i)
print(chr(i))
