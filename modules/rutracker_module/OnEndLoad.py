import os
import sys
import subprocess
series_folder=sys.argv[1]
script_folder=os.path.join(series_folder,"..","scripts")
scriptpath=os.path.join(script_folder,"OnEndLoad.py")
if os.path.exists(scriptpath):
	subprocess.call("python "+scriptpath)