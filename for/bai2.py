#Giải bằng vòng lặp While:
print("Vòng lặp While:")
n = int(input("Nhập n="))
while n > 0:
    a = float(input("Nhập a="))
    b = float(input("Nhập b="))
    if a == 0 and  b== 0:
        print("Vô số nghiệm")
    if  a == 0 and b ! =0:
        print("Vô nghiệm")
    if a != 0 and b != 0:
        print("x=", -b/a)
    n -= 1
print("Kết thúc vòng lặp While")


#Giải bằng vòng lặp For:
print("Vòng lặp For:")
n = int(input("Nhập n="))
for i in range(n):
    a = float(input("Nhập a="))
    b =f loat(input("Nhập b="))
    if a == 0 and b == 0:
        print("Vô số nghiệm")
    if a == 0 and b != 0:
        print("Vô nghiệm")
    if a != 0 and b != 0:
        print("x=", -b/a)
print("Kết thúc vòng lặp For")