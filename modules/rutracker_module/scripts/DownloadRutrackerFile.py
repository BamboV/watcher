import requests
import json
import sys
import os
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,".."))
import settings
import subprocess
import shutil

def DownloadFile(rtcode,label,mediadir):

	torrentfolder=os.path.join(mediadir,"torrent")
	torrentfile = os.path.join(torrentfolder,label+".torrent")
	s= requests.Session()
	r = s.post(settings.rutracker_login_url,
	           data = {'login_username': settings.rutracker_login, 'login_password': settings.rutracker_password, 'login' : '%C2%F5%EE%E4'},
	           
	           )

	rt = s.get(settings.rutracker_download_url+rtcode)
	if not os.path.exists(torrentfolder):
		os.makedirs(torrentfolder)
	if os.path.exists(torrentfile):
		shutil.copy(torrentfile,torrentfile+".old")
	with open(torrentfile, "wb") as code:
	    code.write(rt.content)

	s.close()

	oldfile=torrentfile+".old"
	if os.path.exists(oldfile):
		with open(oldfile,"rb") as old:
			with open(torrentfile,"rb") as new:
				if old.read()==new.read():
					print("There wasn't any updates.")
					return

	seriesdir=os.path.join(mediadir,"series")
	if not os.path.exists(seriesdir):
		os.mkdir(seriesdir)
	

	path_to_torrent_helper=os.path.join(basepath,"..","..","..","helpers","torrenthelper",settings.torrent_helper,"scripts","download.py")
	
	subprocess.Popen("python "+path_to_torrent_helper+" "+torrentfile+" "+seriesdir)
	#subprocess.call(settings.utorrent_path+" /DIRECTORY "+seriesdir+" "+torrentfile)