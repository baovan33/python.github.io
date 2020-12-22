
import random
import string
#Bảng chữ in thường
a = string.ascii_lowercase
#Bảng chữ in hoa
b = string.ascii_uppercase
#Chọn ngẫu nhiên 1 chữ in hoa
t = random.choice(b)
#Random tuổi
age = random.randrange(1, 100)
#Tạo độ dài của tên từ 2 đến 5 chữ
for i in range(random.randrange(1, 5)):
	t += random.choice(a)
dict={'name':t,'age':age}
print(dict)