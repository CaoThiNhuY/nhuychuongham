# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 20:08:10 2024

@author: Admin
"""

#S = 1 + 2 + 3 +......+ n
def tong1(n):
    s=0
    for i in range(1,n+1):
        s +=i
    return s
#S = 1^2 +2^2 +3^2 +......+n^2
def tong2(n):
    s=0
    for i in range(1,n+1):
        s+= i**2
    return s
#S = 1 + 1/2 + 1/3 +......+ 1/n
def tong3(n):
    s=0
    for i in range(1,n+1):
        s+= (1/i)
    return s
#S = 1! + 2! + 3! +......+ n!
def giaithua(x):
    kq=1
    for i in range(1,x+1):
        kq +=i
    return kq
def tong4(n):
    s=0
    for i in range(1,n+1):
        s +=giaithua(i)
    return s
#S = 1 * 2 * 3 *......* n
def tong5(n):
    s=1
    for i in range(1,n+1):
        s *= i
    return s

n=int(input("N="))





if __name__== '__main__':
    print(tong1(3))
    print(tong2(3))
    print(tong3(3))
    print(tong4(3))
    print(tong5(3))