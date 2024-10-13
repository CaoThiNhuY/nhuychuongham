# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:07:31 2024

@author: Student
"""

def kiem_tra(n):
    if n<0 and n%2!=0:
        return -1
    elif n>0 and n%2==0:
        return 1
    return 0

if __name__=="__main__":
    print(kiem_tra(5))