from math import sqrt

a = float(input("Enter 'a': "))
b = float(input("Enter 'b': "))
c = float(input("Enter 'c': "))

perim = (a + b + c)

# p value stands for half perim, whish is needed to calculate area of our triangle

p = (a + b + c)/2
area = sqrt(p*(p - a)*(p - b)*(p - c))

if ((a+b)>c and (b+c)>a and (a+c)>b):
     print """Triangle is possible with these inputs.
            Perimeter: {}
            Area: {}""".format(perim, area)
else:
     print "Trianlge is not possible"
    
