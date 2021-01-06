import os
name_folder=input('name folder: ')
link=os.getcwd()
os.mkdir(name_folder)
os.chdir(name_folder)
name_file= input('name file: ')
egg= open(name_file,'w')
<<<<<<< HEAD:baovan/C4.b13/bai13_2_file.py