#Make a program that tells you how many occurences of one character there in comparison to total number of characters
#have user select which letter they want to compare with
#make a calculation of chosen letter / total characters
#return percentage of how many characters ARE that chosen character
def occurence(a):
    f = open(a, 'r')
    
    #Counting all characters, including punctuation + spaces
    data = f.read().lower().replace(" ", "").replace(".", "").replace("?", "").replace("!", "")
    char_count = len(data)
    print(f'The total number of letters in your file is {char_count}.')
    
    #Getting the count for chosen letter
    answer = str(input('\nFor which letter do you want to know how often it appears? Use lowercase only: '))
    numerator = int(data.count(answer))
    decimal = numerator / int(char_count)
    percent = "{:.2f}".format(decimal * 100)
    print(f"""\nThe letter "{answer}" appears this many times: {numerator}
\nThat means roughly {percent}% of the letters in the text consists of {answer}'s.""")

occurence('letterMAN.txt')
    
