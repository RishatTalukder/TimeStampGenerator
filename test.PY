from pprint import pprint
from pymediainfo import MediaInfo
import os
from collections import defaultdict
import datetime

#get all files in the directory
path = "/home/itvaya/Desktop/recording"
files = os.listdir(path)
 
pprint(files)

file_duration_hash = defaultdict(list)
 
for file in files:
    
    media_info = MediaInfo.parse(f"/home/itvaya/Desktop/recording/{file}")

    for track in media_info.tracks:
        if track.track_type == "Video":
            time1 = datetime.datetime.strptime(track.other_duration[3], "%H:%M:%S.%f") 
            print(time1.time())
            print(track.other_duration[3]) 
            print(datetime.timedelta(hours=0, minutes=0, seconds=0, microseconds=0))
            file_duration_hash[file].append(track.duration)
            file_duration_hash[file].append(track.other_duration[3])
            
    

pprint(file_duration_hash) 
