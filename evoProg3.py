a = float(input('\nWhat is a? - '))
b = float(input('\nWhat is b? - '))
c = float(input('\nWhat is c? - '))
d = (b**2) - (4*a*c)

sqroot = (d ** 0.5)

sol1 = (-b-sqroot)/(2*a)
sol2 = (-b+sqroot)/(2*a)

print('\nThe solution are {0} and {1}'.format(sol1,sol2))

