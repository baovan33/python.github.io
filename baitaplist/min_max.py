import random
n = int(input())
list = random.sample(range(-100,100),n)
print("list= ",list)

# tim max
max = list[1]
for i in range(n - 1):
    if max <= list[i]:
        max = list[i]
print("Max= ",max)

# tim min
min = list[1]
for i in range(n - 1):
    if min >= list[i]:
        min = list[i]
print("Min= ",min)
