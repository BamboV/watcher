import os
rutracker_code=""
label="1" #name of torrent file
extension=".mkv" #extension of video files
directory=os.path.split(os.path.abspath(__file__))[0] #default
path_to_video=os.path.join(directory,"series")
path_to_sub="" #empty if there isn't subtitres
def get_sub_name(ser):  # funcion must return name of subtitres, "ser" is name of video file 
	return ser.split(".")[0]+".ass"