x=[] # 1.tạo một biến x Kiểu list rỗng
x.append(18) # 2.thêm 18 vào x
x.append("Huế") # 3.thêm 'Huế' vào x
y=[12,45,-1,-0.56,"abc"] # 4.tạo list y với các giá trị tương ứng
x=x+y # 5.thêm các giá trị của y vào x
print(x) # 6.in x
# 7.
print('phần tử cuối cùng của x',x[-1])
print('phần tử đầu tiên của x',x[0])
# 8.in các giá trị của phần tử đầu tiên đến phần tử thứ 5 của x
print(x[0:5])
# 9.in các giá trị của phần tử thứ 3 đến phần tử cuối cùng của x
print(x[2:len(x)])
