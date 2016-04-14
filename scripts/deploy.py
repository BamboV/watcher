import os
import sys
import subprocess
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,".."))
import settings
from shutil import copyfile
def Deploy(name,module=""):
	directory=os.path.join(settings.media_dir,name)
	if os.path.exists(directory):
		print("Error "+name+" Already exists")
		return
	os.mkdir(directory)
	os.mkdir(os.path.join(directory,"scripts"))
	if not module=="":
		subprocess.call("python "+os.path.join(settings.module_dir,module,"scripts","deploy.py")+" "+directory)
	#copyfile(os.path.join(settings.templates_dir,"watch_template.py"),os.path.join(directory,"scripts","watch.py"))
	return 

