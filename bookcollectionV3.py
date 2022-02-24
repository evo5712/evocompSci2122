import os
menu_options = {
    1: 'Add book(s)',
    2: 'Check catalog',
    3: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def option1():
     print('Handle option \'Option 1\'')

def option2():
     print('Handle option \'Option 2\'')

def option3():
     print('Handle option \'Option 3\'')

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
    
        if option == 1:
           _ = os.system('cls')
           notDone = True
           allCharacters = []
           while notDone:
              charList =[]
              name = input("\nWhat's the name of the title? ")
              charList.append(name)
              author = input("Who was the author? ")
              charList.append(author)
              genre = input('What is the genre? use "+" if multiple genres. ')
              charList.append(genre)
              pgcnt = input("How many pages are there? ")
              charList.append(pgcnt)
              price = int(input("What's the price in Canada? "))
              taxedBro = "{:.2f}".format(price * 1.13)
              charList.append(taxedBro)
              date = input('Type in date of addition. ')
              charList.append(date)
              allCharacters.append(charList)
              print(f"""
             """)

              answer = input('Have you added all your titles? Type "Yes" or "No": ')
              if answer == "Yes":
                    notDone = False
                    _ = os.system('cls')
              else:
                  print("\nTime for another! ")
        elif option == 2:
            print(allCharacters)
            answer = input('\nGo back to menu? Type "Yes" or "No": ')
            if answer == "Yes":
                  _ = os.system('cls')
                  print_menu
            else:
                print("\nStop messing around, go away. ")
                _ = os.system('cls')
                print_menu
        elif option == 3:
            print("\nPlease never return to this program, ya bum.")
            exit()
        else:
            print('\nInvalid option. Please enter a number between 1 and 3.')

#exec(open("filehere.py").read())
