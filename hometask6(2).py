m = float(input("Enter number m : ")) 
n = float(input("Enter number n : "))

def factorial(x): 
   if x == 0: 
       return 1 
   return factorial(x-1)*x  

def F(y,z):
   result=(factorial(y)*factorial(z))/factorial(y+z)
   return result
F(n,m)

print F(n,m) 
 
