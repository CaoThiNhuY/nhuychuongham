# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:07:45 2024

@author: Admin
"""

def fib(n):
    a,b= 0,1
    while a<n:
        print(a, end=' ')
        a,b=b, a+b
    print()
fib(2018)