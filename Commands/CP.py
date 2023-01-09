import os

os.system("echo cp ")
file_Name=input("Enter the Name of the File you wish to copy")
file_Dir=input("Enter the Directory of the file you wish to copy")
y=os.popen("cp "+file_Name+" "+file_Dir)  #excute ls and store the output in as a string
y=y.read()
print(y)
