x = float(raw_input("Enter x:"))
y = float(raw_input("Enter y:"))
z = float(raw_input("Enter z:"))

res = 0

def polynom(koef, zminna):
    s = 0
    for i in range(31):
      koef=int(raw_input("Enter koefficient:"))
      s = s+koef*(zminna**(30-i))
    return s

res = (((polynom(a, x))**2)-polynom(b, y))/polynom(a, (x+z))
print res


