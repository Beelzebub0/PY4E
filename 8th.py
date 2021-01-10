# Use the file name mbox-short.txt as the file name
fname = input("enter: ")
try:
    fh = open(fname)
except:
    print("Try again:", fname)
    quit()
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    t=line.find("0")
    number= float(line[t:])
    count = count + 1
    total = total + number
average = total/count

print ("Average spam confidence:",average)
