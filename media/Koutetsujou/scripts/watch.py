import subprocess
import os
import sys
base=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(base,".."))
import settings
seriespath=os.path.join(base,"..","series")
with open(os.path.join(base,"unwatched.txt"),"r") as unw:
	lines = unw.readlines()
	if(len(lines)<1):
		print("Nothing too see here.")
		exit()
	ser=lines.pop(0)
videoPath=os.path.join(settings.path_to_video,ser)
#if not os.path.exists(videoPath):
#	print("There isn't "+videoPath)
	#exit()
cmdline="C:\\Program Files\\MPC-HC\\mpc-hc64.exe \""+videoPath+"\""
if not settings.path_to_sub == "":
	subPuth=os.path.join(settings.path_to_sub,settings.get_sub_name(ser))
	if os.path.exists(subPuth):
 		cmdline=cmdline+" /sub \""+subPuth+"\""

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