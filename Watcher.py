import os
import sys
import subprocess
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, "scripts")
import settings
import deploy


if(sys.argv[1]=="watch"):
	watchpath = os.path.join(basepath, "scripts", "watch.py")
	if os.path.exists(watchpath):
		subprocess.call("python "+watchpath+" "+sys.argv[2]+" "+basepath)
	else:
		print("Error! Script "+watchpath+" doesn't exists.")
	exit()
if(sys.argv[1]=="init"):
	if len(sys.argv)>3:
		deploy.Deploy(sys.argv[2],sys.argv[3])
	else:
		deploy.Deploy(sys.argv[2])
	exit()
if(sys.argv[1]=="download"):
	dpath = os.path.join(basepath, "scripts", "download.py")
	if os.path.exists(dpath):
		subprocess.call("python "+dpath+" "+sys.argv[2]+" "+basepath)
	else:
		print("Error! Script "+dpath+" doesn't exists.")
	exit()
if sys.argv[1]=="list":
	lines=os.listdir(os.path.join(basepath,"media"))
	for line in lines:
		print(line)
	exit()
if sys.argv[1]=="unwatched":
	lines=os.listdir(os.path.join(basepath,"media"))
	for line in lines:
		linepath = os.path.join(basepath,"media",line,"scripts","unwatched.txt")
		if(os.path.exists(linepath)):
			with open(linepath,"r") as unw:
				strs = unw.readlines()
				if(len(strs)>0):
					print(line+"\n")
					for st in strs:
						print("\t-"+st)
	exit()

	
print("Error! Where isn't \""+sys.argv[1]+"\" command.")

