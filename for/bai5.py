import math


list = [1, 2, 3, -5, 0.1, 0]
for i in range(len(list)):
    print("List[",i,"] =", list[i])
for i in range(len(list)):
    if list[i] > 0:
        print("Log(",list[i],") =" ,math.log(list[i]))


print("Kết thúc")