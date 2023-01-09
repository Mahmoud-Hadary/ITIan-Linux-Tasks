import os
while(1):
	check = int(input("Enter 1 if you wish Create a file;\n press 2 if you want Concatinate a file;\n press 3 if want to Desplay a file in reverse\npress 0 if you wish to close;\n"))
	if (check == 1):
		filename= input("Enter the File name you wish to name your file")
		os.system("echo cat > "+filename)
		
		#_Curr_Dir=os.popen("cat > "+filename)
		#_Curr_Dir=_Curr_Dir.read()
		#print(_Curr_Dir)
	elif (check == 2):
		filename = input("Enter the first File name you wish to Concatinate")
		filename2 = input("Enter the Second File name you wish to Concatinate")
		filename1= input("Enter the File name you wish to name your file")
		#filename1.txt filename2.txt > filename3.txt
		#os.system("echo cat "+filename+" "+filename2+" > "+filename1)
		
		_Curr_Dir=os.popen("cat "+filename+" "+filename2+" > "+filename1)
		_Curr_Dir=_Curr_Dir.read()
		print(_Curr_Dir)
	elif (check == 3):
		filename = input("Enter the first File name you wish to Read in reverse")
		os.system("echo tac > "+filename)
		#os.chdir(_Dir)
		#_Curr_Dir=os.popen("tac > "+filename)
		#_Curr_Dir=_Curr_Dir.read()
		#print(_Curr_Dir)
	elif (check == 0):
		break 