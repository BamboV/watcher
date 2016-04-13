import sys
import os
basepath=os.path.split(os.path.abspath(__file__))[0]
sys.path.insert(0, os.path.join(basepath,".."))
import settings
from shutil import copyfile
folder=sys.argv[1]
os.mkdir(os.path.join(folder,"series"))
copyfile(os.path.join(settings.templates_dir,"settings_template.py"),os.path.join(folder,"settings.py"))
copyfile(os.path.join(settings.templates_dir,"download_template.py"),os.path.join(folder,"scripts","download.py"))
copyfile(os.path.join(settings.templates_dir,"watched_template.txt"),os.path.join(folder,"scripts","watched.txt"))
copyfile(os.path.join(settings.templates_dir,"unwatched_template.txt"),os.path.join(folder,"scripts","unwatched.txt"))
copyfile(os.path.join(settings.templates_dir,"watch_template.py"),os.path.join(folder,"scripts","watch.py"))
copyfile(os.path.join(settings.templates_dir,"OnEndLoad_template.py"),os.path.join(folder,"scripts","OnEndLoad.py"))
