import os
import sys
import subprocess
basepath= sys.argv[2]
targetpath=sys.argv[1]
scriptPath=os.path.join(basepath,"media",targetpath,"scripts","watch.py")
subprocess.call("python "+scriptPath)
