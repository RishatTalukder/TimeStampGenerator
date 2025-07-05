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
            file_duration_hash[file].append(track.duration)
            file_duration_hash[file].append(track.other_duration[3])

    

pprint(file_duration_hash)

#calculate the total duration of the files
total_duration = 0
for key in file_duration_hash:
    total_duration += file_duration_hash[key][0]

print(f"Total duration of the files is {datetime.timedelta(milliseconds=total_duration)}")

