import os
import sys
import subprocess
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,"scripts"))
import settings
import deploy
import deploymodule

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
if sys.argv[1]=="settings":
	if len (sys.argv)<3:
		os.system(os.path.join(basepath,"settings.py"))
	else:
		if sys.argv[2]=="-m" and len(sys.argv)>3:
			settings_path=os.path.join(basepath,"modules",sys.argv[3],"settings.py")
		else:
			settings_path=os.path.join(basepath,"media",sys.argv[2],"settings.py")
		if os.path.exists(settings_path):
			os.system(settings_path)
		else:
			print("There isn't settings file for "+(sys.argv[2] if len(sys.argv)==3 else sys.argv[3]))
	exit()
if sys.argv[1]=="initmodule":
	if len(sys.argv)==3:
		deploymodule.Deploy(sys.argv[2])
	else:
		deploymodule.Deploy(sys.argv[2],sys.argv[3])
	exit()
	
print("Error! Where isn't \""+sys.argv[1]+"\" command.")

