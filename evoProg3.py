import cmath
    
a = float(input('\nWhat is a? - '))
b = float(input('\nWhat is b? - '))
c = float(input('\nWhat is c? - '))
    
d = (b**2) - (4*a*c)
    
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
    
print('\nThe solution are {0} and {1}'.format(sol1,sol2)) 
