# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 22:21:21 2024

@author: nhuy
"""

import math
#52a
def canbacn(x, n):
    return x ** (1/n)
#52b chuoi hoac chu so, giu lai so 0 dang truoc
def daoso(n):
    return str(n[::-1])
#so: mat so 0 dang truoc
def daoso(n):
    return int(str(n)[::-1])
#cach 3 so
def dao (n):
    dao = 0
    while n>0:
        dao= dao * 10 + n % 10
        n //= 10
    return dao
#52c
def ktra_chinhphuong(n):
    return int(math.sqrt(n))**2 == n
#52d
def ktr_nguyento(n):
    if n<2:
        return False
    for i in range (2, n):
        if n%i == 0:
            return False
    return True
#52e
def tichsole(n):
    tich= 1
    for i in str(n): #str la tinh chu so le phai dung str(string), neu de khong noi la CHU SO thi dung for i ... range(1, n+1)
        if int(i)%2 !=0:
            tich *= int(i)
    return tich
#52f
def tong_ngto_nho_n(n):
    tong_ngto = 0
    for i in range(2, n):
        if ktr_nguyento(i):
            tong_ngto += i
    return tong_ngto
#52g 
def tong_chinhphuong(n):
    tong_cp = 0
    for i in range(1, n):
        if ktra_chinhphuong(i):
            tong_cp += 1
    return tong_cp
#52h
def tong_uoc(n):
    tong = 0
    for i in range(1, n+1):
        if n%i == 0:
            tong += i
    return 

if __name__== "__main__":
    print(canbacn(8,3))
    print(daoso(1234560))
    print(dao(124560))
    print(ktra_chinhphuong(2))
    print(ktr_nguyento(2))
    print(tichsole(3))
    print(tong_ngto_nho_n(2))
    print(tong_chinhphuong(9))
    print(tong_uoc(15))