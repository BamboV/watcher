with open("unwatched.txt","r") as unw:
	lines = unw.readlines()
	ser=lines.pop(0)
print("watching "+ser)
while True:
	a=input("Переместить в просмотрено?(Y/N)")
	if a=="y" or "Y":
		with open("watched.txt","a") as wached:
			wached.write(ser)
		with open("unwatched.txt","w") as unw:
			unw.writelines(lines)
		break
	if a=="n" or "N":
		break	