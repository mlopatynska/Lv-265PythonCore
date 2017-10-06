def list(parameter, variable):
    s=0
    for i in range(31):
        s = s + parameter*(variable**(30-i))
    return s

a = float(raw_input("Enter a: "))
x = float(raw_input("Enter x: "))
b = float(raw_input("Enter b: "))
y = float(raw_input("Enter y: "))
c = float(raw_input("Enter c: "))
z = float(raw_input("Enter z: "))

result = (((list(a,x))**2)-list(b,y))/list(c,(x+z))
print result
