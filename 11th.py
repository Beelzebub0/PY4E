
fname = input("Enter file:")
try:
    fn = open(fname)
except:
    print("cannot open", fname)
    quit()

counts = dict()
for line in fn:
    words = line.split()
    if len(words) < 3 or words[0] != "From": continue
    lst = list()
    lst.append(words[1])
    print(lst)
    for word in lst:
        counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
