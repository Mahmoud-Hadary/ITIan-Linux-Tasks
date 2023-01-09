import os

os.system("echo 1 ls ")
y=os.popen("ls")  #excute ls and store the output in as a string
y=y.read()
print(y)

