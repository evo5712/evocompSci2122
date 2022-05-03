def encrypt():
    print("Type out what you would like to encrypt below.\n")
    msg = input()
    shift = int(input('\nWhat number would you like the shift to be? - '))
    secret = ""
    for c in msg:
        if c.isupper() or c.islower():
            c_index = ord(c) - ord("A")
            new_index = (c_index) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            secret = secret + new_character
        else:
            secret += c
    print(f'\nYour encrypted message is: {secret}')
    
encrypt()
            

        
        
        
        

