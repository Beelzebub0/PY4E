import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

sum=0
site = input('Enter location: ')
osite = urllib.request.urlopen(site)
data = osite.read()
tree = ET.fromstring(data)

for x in tree.findall('comments/comment'):
    numb = int(x.find('count').text)
    sum=sum+numb
print(sum)
