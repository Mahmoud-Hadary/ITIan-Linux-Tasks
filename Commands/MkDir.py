import os

os.system("echo mkdir")
filename=input("Enter The foulder name you will be creating")
y=os.popen("mkdir "+ filename)  #excute ls and store the output in as a string
y=y.read()
print(y)

