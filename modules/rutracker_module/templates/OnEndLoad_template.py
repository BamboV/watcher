import os
import subprocess
import sys
import shutil

base=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(base,".."))
import settings
series=os.listdir(settings.path_to_video)
watchedpath=os.path.join(base,"watched.txt")
if os.path.exists(watchedpath):
	with open(os.path.join(base,"watched.txt"), "r") as code:
		with open(os.path.join(base,"unwatched.txt"),"a+") as unw:
			watched=code.read()
			unw.seek(0)
			unwached=unw.read()
			for s in series:
				if s not in watched and s not in unwached and settings.extension in s:
					unw.write(s+"\n")

		


