import os
import sys
import subprocess
load_folder=sys.argv[1]
media_folder = load_folder.split("series")[0]

script_folder=os.path.join(media_folder,"scripts")
scriptpath=os.path.join(script_folder,"OnEndLoad.py")
if os.path.exists(scriptpath):
	subprocess.call("python "+scriptpath)