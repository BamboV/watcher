import subprocess
import os
import sys
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,".."))
import settings
cmdstr="python "+os.path.join(basepath,"..","..","..","modules","rutracker_module","scripts","download.py")+" "+settings.rutracker_code+" "+settings.label+" "+settings.directory

subprocess.call(cmdstr)