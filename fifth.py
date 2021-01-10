def computepay(h,r):
    if h <= 40:
        xp = h*r
    if h >= 40:
        xp = (1.5*r*(h-40)+(40*r))
    return xp
hrs = input("Enter Hours:")
h = float(hrs)
rte = input("Enter Rate:")
r = float(rte)
p = computepay(h,r)
print("Pay",p)
