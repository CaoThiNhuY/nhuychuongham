# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:10:26 2024

@author: Student
"""

def ktra_gtri():
    gtri=input('nhap gia tri: ')
    if gtri.replace('.','',1).replace('-','',1).isdigit():
        gtri=float(gtri)
    if -86<= gtri <= 90:
        return gtri
    print("khong hop le, nhap lai")
    return ktra_gtri()
if __name__=="__main__":
    print(ktra_gtri())