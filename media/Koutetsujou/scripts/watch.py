import subprocess
import os
base=os.path.split(os.path.abspath(__file__))[0]
seriespath=os.path.join(base,"..","series")
with open(os.path.join(base,"unwatched.txt"),"r") as unw:
	lines = unw.readlines()
	ser=lines.pop(0)
cmdline="C:\\Program Files\\MPC-HC\\mpc-hc64.exe \""+os.path.join(seriespath,ser)+"\""

subprocess.call(cmdline)
while True:
	a=input("Переместить в просмотрено?(Y/N)")
	if a=="y" or a=="Y":
		with open(os.path.join(base,"watched.txt"),"a") as wached:
			wached.write(ser)
		with open(os.path.join(base,"unwatched.txt"),"w") as unw:
			unw.writelines(lines)
		break
	if a=="n" or a=="N":
		break