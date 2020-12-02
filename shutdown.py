import os
import time
while 1 == 1:
    a = input("Tắt máy (y/n): ")
    if (a == "Y" or a == "y" ):
        break
    time.sleep(30)
os.system('shutdown -s')
