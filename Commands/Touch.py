import os

os.system("echo touch ")
filename=input("Enter The file name you will be creating")
y=os.popen("touch "+ filename)  #excute ls and store the output in as a string
y=y.read()
print(y)

