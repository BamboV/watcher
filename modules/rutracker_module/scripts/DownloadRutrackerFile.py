import requests
import json
import sys
import os
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,".."))
import settings
import subprocess


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

	with open(torrentfile, "wb") as code:
	        code.write(rt.content);
	    

	s.close()
	seriesdir=os.path.join(mediadir,"series")
	subprocess.call(settings.utorrent_path+" /DIRECTORY "+seriesdir+" "+torrentfile)