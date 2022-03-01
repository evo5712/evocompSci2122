while True:
    print("1 -- Add book(s)")
    print("\n2 -- Look at last entry")
    print("\n3 -- Exit")
    choice = float(input("\nEnter your choice:  "))
    if choice == 1:
        notDone = True
        fullInventory = []
        while notDone:
          charList =[]
          name = input("\nWhat's the name of the title? ")
          charList.append(name)
          author = input("\nWho was the author? ")
          charList.append(author)
          genre = input('\nWhat is the genre? use "+" if multiple genres. ')
          charList.append(genre)
          pgcnt = input("\nHow many pages are there? ")
          charList.append(pgcnt)
          price = float(input("\nWhat's the price in Canada? "))
          taxedBro = "{:.2f}".format(price * 1.13)
          charList.append(taxedBro)
          date = input('\nType in date of addition. ')
          charList.append(date)
          fullInventory.append(charList)
          print(f"""
          """)

          answer = input('Have you added all your titles? Type "Yes" or "No": ')
          if answer == "Yes":
                 notDone = False
          else:
              print("\nTime for another! ")
    if choice == 2:
        print("\nYour latest entry into our catalogue was:")
        print("\n****************************************")
        print("\nBook: ", charList[0])
        print("\nAuthor: ", charList[1])
        print("\nGenre(s) ", charList[2])
        print("\nPage Count: ", charList[3])
        print("\nPrice, with tax: ", charList[4])
        print("\nDate added to inventory: ", charList[5])
        print("\n****************************************")

        answer = input('\nWould you like to go back to the main menu? Type "Yes" or "No": ')
        if answer == ("Yes"):
              notDone = False
              print("\nOff you go!")
        else:
            print("\nYou're going back to the menu, whether you like it or not.")
    if choice == 3:
        print("\nGet out of here, NERD. ")
        exit()
    if choice > 3:
        print("\nInvalid input, please try again. ")
        
        
              
