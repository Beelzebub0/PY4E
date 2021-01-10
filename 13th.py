
fname = input("enter your file:")
try:
    fh = open(fname)
except:
    print("cannot open", fname)
    quit()
import re
x=list()
for line in fh:
     y = re.findall('[0-9]+',line)
     x = x+y
sum=0
for z in x:
    sum = sum + int(z)
print(sum)
