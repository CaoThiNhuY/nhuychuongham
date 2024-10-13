# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 23:01:52 2024

@author: Admin
"""


chieu_dai = int(input("Nhập chiều dài hình chữ nhật: "))
chieu_rong = int(input("Nhập chiều rộng hình chữ nhật: "))
def tinh_chu_vi_dien_tich(chieu_dai, chieu_rong):
    chu_vi = 2 * (chieu_dai + chieu_rong)
    dien_tich = chieu_dai * chieu_rong
    return chu_vi, dien_tich
chu_vi, dien_tich = tinh_chu_vi_dien_tich(chieu_dai, chieu_rong)
print(f"Chu vi hình chữ nhật là: {chu_vi}")
print(f"Diện tích hình chữ nhật là: {dien_tich}")

def ve_hinh_chu_nhat(chieu_dai, chieu_rong):
    for i in range(chieu_rong):
        print('* ' * chieu_dai)
# Vẽ hình chữ nhật
print("Hình chữ nhật:")
ve_hinh_chu_nhat(chieu_dai, chieu_rong)
