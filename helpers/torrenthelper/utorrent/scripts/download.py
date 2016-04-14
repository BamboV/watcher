import sys
import subprocess
import os
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,".."))
import settings
torrent_path=sys.argv[1]
download_path=sys.argv[2]
subprocess.call("\""+settings.utorrent_path+"\" /DIRECTORY \""+download_path+"\" \""+torrent_path+"\"")