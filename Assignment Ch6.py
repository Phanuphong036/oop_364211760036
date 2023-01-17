"""
OOP Exercise Chapter 6

1. จงเขียนโปรแกรมภาษาไพธอนเพื่อสร้างคลาสพาหนะชื่อ Vehicle ที่ประกอบไปด้วยคุณลักษณะ (attributes) คือ
ยี่ห้อรถ (brand)
รุ่นรถ (model)
สีรถ (color)
ความรเร็วสูงสุด (max speed)
ราคา (price)
"""
Vahicle_store = []
num = int(input('Vahicle? :'))

for x in range(num):
    brand = input('ยี่ห้อ:')
    model = input('รุ่นรถ: ')
    color = input('สีรถ: ')
    speed = input('ความเร็วสูงสุด: ')
    price = float(input('ราคา: '))

    # 1
    b = Vahicle(brand,model,color,speed,price)
    Vahicle_store.append(b)
    # 2
    #book_store.append(Book(bookname,price,auther,publisher))

def display_Vahicle(Vahicle):
    print('จำนวนรถ:',len(Vahicle))
    for x in Vahicle:
        x.Vahicle_detail()

display_Vahicle(Vahicle_store)
"""

2.จากข้อที่ 1 เขียนโปรแกรมเพื่อสร้างวัตถุ (object) จากคลาส Vehicle โดยรับข้อมูลจากผู้ใช้ตามคุณลักษณะ (attributes)ของคลาส
จากนั้นแสดงข้อมูลทางหน้าจอภาพ

15 นาที
"""
