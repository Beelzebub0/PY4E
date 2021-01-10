score = input("Enter Score: ")
xs = float(score)
try:
    xs = float(score)
except:
    print("Error, enter numeric input")
    quit()
if xs < 0:
    print("Error")
if xs > 1:
    print("Error")
elif xs >= 0.9:
    print("A")
elif xs >= 0.8:
    print("B")
elif xs >= 0.7:
    print("C")
elif xs >= 0.6:
    print("D")
elif xs < 0.6:
    print("F")
