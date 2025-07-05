import datetime

time1 = 12345

time = datetime.datetime.fromtimestamp(time1, datetime.UTC)

print(time.time()) 