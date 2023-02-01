"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)
"""

"""

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""

Vahicle_store = []
num = int(input('Vahicle? :'))

for x in range(num):
    brand = input('ยี่ห้อ:')
    model = input('รุ่นรถ: ')
    color = input('สีรถ: ')
    speed = input('ความเร็วสูงสุด: ')
    price = float(input('ราคา: '))

    print("ยี่ห้อรถ : ",brand)
    print("รุ่นรถ : ",model)
    print("สีรถ : ",color)
    print("ความรเร็วสูงสุด : ",speed)
    print("ราคา : ",price)