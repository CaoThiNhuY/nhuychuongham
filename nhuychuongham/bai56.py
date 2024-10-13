# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:40:55 2024

@author: Admin
"""

import math
def chuvi_dt(hinh, pheptinh,*args, **kwargs):
    if hinh == 'vuong':
        canh = args[0]
        return canh*4 if pheptinh == 'chuvi' else canh**2
    elif hinh == 'chunhat':
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) if pheptinh == 'chuvi' else dai*rong
    elif hinh == 'tron':
        bankinh = args[0]
        return 2*math.pi*bankinh if pheptinh == 'chuvi' else math.pi*bankinh**2
    else:
        return "hình chưa đúng"
    
    
    
    
    
#if __name__== '__main__':
print('chu vi hinh vuong:', chuvi_dt('vuong', 'cv',5))
print('dien tich hinh vuong:', chuvi_dt('vuong', 'dt',5))
print('chu vi hinh chu nhat:',  chuvi_dt('chunhat', 'cv',5,4))
print('dien tich hinh chu nhat:',  chuvi_dt('chunhat', 'dt',5,4))
print('chu vi hinh tron:',  chuvi_dt('tron', 'cv',5))
print('dien tich hinh tron:',  chuvi_dt('tron', 'dt',5))
