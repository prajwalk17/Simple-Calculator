hrs = input("Enter Hours:")
h = float(hrs)
rae = input("Enter rate:")
r = float(rae)

if h <= 40:
    pay = h*r
    
elif h > 40:
    pay = 40*r + (h-40)*r*1.5
    
print(pay)