import os
print(dir(os))

os.getcwd()
os.listdir()
os.chdir("D:\\bt_c3.b13_os_file")
print(os.getcwd())
os.mkdir('vv')
print(os.listdir())
os.rmdir('vv')
print(os.listdir())
os.remove("New Text Document.txt")
print(os.listdir())

list1=[]
list2=[]
for (a,b,c) in os.walk('C:\\'):
	print(a) 
	print(b) 
	print(c) 

for (a,b,c) in os.walk('C:\\'):
	if b!=[]:
		list2.append(b)
	if c!=[]:
		list1.append(c)
print(list1)	
print(list2)