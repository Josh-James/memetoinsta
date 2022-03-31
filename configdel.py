import shutil
import os
def deletepath():
    if os.path.exists("/memetoinsta/memes/config"):
        shutil.rmtree("/memetoinsta/memes/config")
        print("Path removed")
    else:
        print("No config file available")
    if os.path.exists("/memetoinsta/memes/image.jpg.REMOVE_ME"):
        os.remove("/memetoinsta/memes/image.jpg.REMOVE_ME")
    else:
        print("No REMOVE_ME file available")
    if os.path.exists("/home/pi/config"):
        shutil.rmtree("/home/pi/config")
        print("Path removed")
    else:
        print("No config file available")
    if os.path.exists("/home/pi/config"):
        shutil.rmtree("/home/pi/config")
    else:
        print("No config file")

deletepath()