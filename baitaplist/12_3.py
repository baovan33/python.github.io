import random
import numpy as np
import string
#Tạo bảng chữ cái in hoa
a=string.ascii_uppercase
#Tạo bảng chữ cái in thường
b=string.ascii_lowercase
#Random số phần tử của List từ 50 đến 100
n=random.randrange(50,101)
#Tạo List dạng dictionary có cấu trúc {0.0} với n phần tử
listdict=list(np.zeros(n))
#Hàm tạo tên
def name():
    k= random.choice(a)
    for i in range(random.randrange(2,8)):
        k+= random.choice(b)
    return k
#Hàm tạo tuổi
def age():
    age= random.randrange(0,100)
    return age
#Gán các giá trị tên và tuổi vào List
for i in range(len(listdict)):
    listdict[i]={'name':name(),'age':age()}
print(listdict)