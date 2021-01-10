fname= input('Enter a file name: ')
fh = open(fname)
lst = list()
for line in fh:
    word= line.split()    
    for element in word:
        if element not in lst:
            lst.append(element)
print(sorted(lst))
