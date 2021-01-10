import json
import urllib.request, urllib.parse, urllib.error

count = 0

site = input('Enter location: ')
uh = urllib.request.urlopen(site)
print ("retrieving URL")
data= uh.read().decode()

names = json.loads(data)
for item in names["comments"]:
	number = int(item["count"])
	count = count + number
print (count)
