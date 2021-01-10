
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("can't open", fname)
    quit()
count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From") : continue
    if line.startswith("From:") : continue
    words = line.split()
    print(words[1])
    count = count+1
print("There were", count, "lines in the file with From as the first word")
