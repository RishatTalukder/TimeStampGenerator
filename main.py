from pprint import pprint
from pymediainfo import MediaInfo
import os

#get all files in the directory
path = "/home/itvaya/Desktop/recording"
files = os.listdir(path)

pprint(files)


def format_duration(duration):
    hours = int(duration / 3600)
    minutes = int((duration % 3600) / 60)
    seconds = int(duration % 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"


for file in files:
    
    media_info = MediaInfo.parse(f"/home/itvaya/Desktop/recording/{file}")
    pprint(media_info.tracks)
    for track in media_info.tracks:
        if track.track_type == "Video":

            print("Duration (raw value):", track.duration)
            print("Duration (other values:")
            pprint(track.other_duration[4])   
