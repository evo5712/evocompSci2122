def product(a):
    f = open(a, "r")
    
    product = 1
    for line in f:
        product = product * int(line)
        
    print(product)
    print('Eric says, "I definitely did not copy you Mr. Green, please do not destroy my report card.')
    
    f.close()

