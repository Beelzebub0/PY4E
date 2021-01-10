name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lst=list()
counts=dict()
for line in handle :
    if line.startswith("From "):
        line=line.strip().split()
        hours=line[5]
        hours=hours[:2]
        lst.append(hours)

for hour in lst :
    counts[hour]=counts.get(hour,0)+1

for k,v in sorted(counts.items()) :
    print(k,v)
