import os
while(1):
	check = int(input("Enter 1 if you wish to go back a dir;\n press 2 if you want to go to home;\n press 3 if want to go to a cpecific directory\npress 0 if you wish to close;\npress 4 to check your keyboard inputs\nto check the wifi press 5\n"))
	if (check == 1):
		os.system("echo cd ..")
		os.chdir("..")
		_Curr_Dir=os.popen("pwd")
		_Curr_Dir=_Curr_Dir.read()
		print(_Curr_Dir)
	elif (check == 2):
		os.system("echo cd ~")
		os.chdir("/")
		_Curr_Dir=os.popen("pwd")
		_Curr_Dir=_Curr_Dir.read()
		print(_Curr_Dir)
	elif (check == 3):
		_Dir=input("Enter your Desired Directory")
		os.system("echo cd "+_Dir)
		os.chdir(_Dir)
		_Curr_Dir=os.popen("pwd")
		_Curr_Dir=_Curr_Dir.read()
		print(_Curr_Dir)
	elif (check == 4):
		#os.popen("touch KeyboardLogger.txt") 
		os.popen("ln -s /dev/input/event1  KeyboardLogger.txt")
	elif (check == 5):
		#os.popen("touch Console.txt") 
		os.popen("ln -s /dev/stdout  Console.txt")
		#os.popen("cat Console.txt")
	elif (check == 6):
		os.popen("touch Network.txt") 
		os.popen("sudo lshw -C network > Network.txt")
		os
	elif (check == 7):
		os.popen("touch HardwareData.txt") 
		os.popen("sudo lshw > HardwareData.txt")
	elif (check == 0):
		break 