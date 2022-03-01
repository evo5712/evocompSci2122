#Please note that the program only works when you add 2 books.

while True:
    print("1 -- Add book(s)")
    print("\n2 -- Look at catalogue")
    print("\n3 -- Print last entry")
    print("\n4 -- Exit")
    choice = float(input("\nEnter your choice:  "))
    if choice == 1:
        notDone = True
        fullInventory = []
        while notDone:
          bookOne =[]
          name = input("\nWhat's the name of the title? ")
          bookOne.append(name)
          author = input("\nWho was the author? ")
          bookOne.append(author)
          genre = input('\nWhat is the genre? use "+" if multiple genres. ')
          bookOne.append(genre)
          pgcnt = input("\nHow many pages are there? ")
          bookOne.append(pgcnt)
          price = float(input("\nWhat's the price in Canada? "))
          taxedBro = "{:.2f}".format(price * 1.13)
          bookOne.append(taxedBro)
          date = input('\nType in date of addition. ')
          bookOne.append(date)
          fullInventory.append(bookOne)
          print(f"""
          """)

          answer = input('Have you added all your titles? Type "Yes" or "No": ')
          if answer == "Yes":
                 notDone = False
          else:
              print("\nTime for another! ")
              while notDone:
                bookTwo =[]
                name2 = input("\nWhat's the name of the title? ")
                bookTwo.append(name2)
                author2 = input("\nWho was the author? ")
                bookTwo.append(author2)
                genre2 = input('\nWhat is the genre? use "+" if multiple genres. ')
                bookTwo.append(genre2)
                pgcnt2 = input("\nHow many pages are there? ")
                bookTwo.append(pgcnt2)
                price = float(input("\nWhat's the price in Canada? "))
                taxedBro2 = "{:.2f}".format(price * 1.13)
                bookTwo.append(taxedBro2)
                date2 = input('\nType in date of addition. ')
                bookTwo.append(date2)
                fullInventory.append(bookTwo)
                print(f"""
                """)

                answer = input('Have you added all your titles? Type "Yes" or "No": ')
                if answer == "Yes":
                    notDone = False
                else:
                    print("\nThere's no more room for extra books. You need to go. ")
                    notDone = False
    if choice == 2:
        print(f"""\nThe books that you've catalogued are: {name} , {name2}""")

        answer = input(f"\nWould you like to search up {name}, {name2}, or both? - ")
        if answer == (f"{name}"):
           print("\nBook: ", bookOne[0])
           print("\nAuthor: ", bookOne[1])
           print("\nGenre(s) ", bookOne[2])
           print("\nPage Count: ", bookOne[3])
           print("\nPrice, with tax: ", bookOne[4])
           print("\nDate added to inventory: ", bookOne[5])
        if answer == (f"{name2}"):
           print("\nBook: ", bookTwo[0])
           print("\nAuthor: ", bookTwo[1])
           print("\nGenre(s) ", bookTwo[2])
           print("\nPage Count: ", bookTwo[3])
           print("\nPrice, with tax: ", bookTwo[4])
           print("\nDate added to inventory: ", bookTwo[5])
        if answer == "both":
            print(f"""
  Book #1: {name}                  
                              
  Author: {author} 
                              
  Genre(s): {genre}   
                              
  Page Count: {pgcnt}           
                              
  Price (CAD): {taxedBro}          
                              
  Date Added: {date}               

---------------------------

  Book #2: {name2}

  Author: {author2}

  Genre(s): {genre2}

  Page Count: {pgcnt2}

  Price (CAD): {taxedBro2}

  Date Added: {date2}
 """)
       
        answer = input('\nWould you like to go back to the main menu? Type "Yes" or "No": ')
        if answer == ("Yes"):
              notDone = False
              print("\nOff you go!")
        else:
            print("\nYou're going back to the menu, whether you like it or not.")
    if choice == 3:
     print("\nHere is your latest entry into our catalogue!")
     print(f"""

*******************************************

Title: {name2}

Author: {author2}

Genre(s): {genre2}

Page Count: {pgcnt2}

Price (CAD): {taxedBro2}

Date Added: {date2}

*******************************************
""")
    if choice == 4:
        print("\nGet out of here, NERD. ")
        exit()
    if choice > 4:
        print("\nInvalid input, please try again. ")        

        
        
              


              

