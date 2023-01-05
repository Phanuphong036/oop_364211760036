"""
Student Name:{Phanuphong Sutthiphibun}
ID:{364211760036}
Group: {MIT212}
"""

"""
Example:
class Book
attributes: book_name(str),price(float),auther(str),publisher(str)  
"""

#create class
class Book:
    def __init__(self,bookname,price,auther,publisher):
        # object attributes
        self.bookname = bookname
        self.price = price
        self.auther = auther
        self.publisher = publisher
    def book_detail(self):
        print(f'Book name: {self.bookname} Price: {self.price} THB'
              f'Auther:  ')


#create odject
b1 = Book("ความมั่งคั่งปฏิวัติ (REVOLUTIONARY WEALTH)",250.00,"ALVIN TOFFLER, HEIDI TOFFLER",'RW')
b2 = Book("NOW I UNDERSTAND",349.00,"ต้นกล้า นัยนา",'NIU')
print(b1.bookname)
print(b1.price)
print(b1.auther)
print(b1.publisher)

print(b2.bookname)
print(b2.price)
print(b2.auther)
print(b2.publisher)


#using method from class
b1.book_detail()
b2.book_detail()
#store objects into list
mybook = list([b1,b2])
mybook.append(b1)
mybook.append(b2)
print("Display books from list:")
for x in range(len(mybook)):
    print(mybook[x].book_detail())