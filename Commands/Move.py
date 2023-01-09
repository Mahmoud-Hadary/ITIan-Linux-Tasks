import os

os.system("echo mv ")
file_Name=input("Enter the Name of the File you wish to Move")
file_Dir=input("Enter the Directory of the file you wish to Move")
y=os.popen("mv "+file_Name+" "+file_Dir)  #excute ls and store the output in as a string
y=y.read()
print(y)
