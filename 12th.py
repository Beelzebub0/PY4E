fname = input("Enter file:")
try:
    fh = open(fname)
except:
    print("cannot open", fname)
    quit()
lst=list()
counts=dict()
for line in fh :
    if line.startswith("From "):
        line=line.strip().split()
        hours=line[5]
        hours=hours[:2]
        lst.append(hours)
for hour in lst :
    counts[hour]=counts.get(hour,0)+1

for k,v in sorted(counts.items()) :
    print(k,v)
