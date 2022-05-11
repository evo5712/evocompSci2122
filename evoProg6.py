def encrypt(a):
    f = open(a, 'r')
    secret = ""
    for line in f:
        string = line
    for shift in range(26):
        for c in string:
            if c.isupper() or c.islower():
                c_index = ord(c) - ord("A")
                new_index = (c_index + shift) % 26
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
                secret = secret + new_character
            else:
                secret += c
        print(f'\nWe revealed the encrpytion to be {secret}.', end = '')
        secret = ''
        
        
encrypt('proj6 text.txt')



