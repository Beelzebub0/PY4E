hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
if h <= 40:
    print(h*r)
if h > 40:
    print(1.5*r*(h-40)+(40*r))
