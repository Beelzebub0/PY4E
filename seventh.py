# Use words.txt as the file name
try:
    fname = input("Enter file name: ")
except:
    print("Error", fname)
fh = open(fname)
for cek in fh:
    cek = cek.rstrip()
    if cek.startswith('Our'):
        print(cek.upper())
