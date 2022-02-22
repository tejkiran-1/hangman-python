import random
import string

print("H A N G M A N\n")

myList = ['python', 'java', 'kotlin', 'javascript']

choice = random.choice(myList)
guess = len(choice) * "-"
#print(guess)

set_of_letters = set(choice)
tries = 0
verify = ''
verify2 = ''
list_user = set()
list_user2 = set()
yes = input("Type \"play\" to play the game, \"exit\" to quit:")
while True:
    
    print()
    print(guess)
    user = input("Input a letter: ")
    
    if user not in string.ascii_lowercase:
        if len(user) != 1:
            print("You should input a single letter")
            #tries += 1
            continue
        else:
            print("Please enter a lowercase English letter")
            #tries += 1
            continue
            

    if user in set_of_letters and user not in list_user:
        get_index = choice.find(user)
        get_index2 = choice.rfind(user)
        guess = guess[:get_index] + user + guess[get_index+1:]
        guess = guess[:get_index2] + user + guess[get_index2+1:]
        list_user.add(user)
        #print(guess)
    elif  user in list_user or set_of_letters != set(guess):
        #if set_of_letters != set(guess):
        if user in list_user:
            print("You've already guessed this letter\n")
            print(guess)
        else:
            if user in list_user2:
                print("You've already guessed this letter\n")
            else:
                print("That letter doesn't appear in the word")
                tries += 1
                list_user2.add(user)
            
        if tries == 8:
            print("You lost!")
            break
 
    if tries == 8  or set_of_letters == set(guess):
        if set_of_letters == set(guess):
            print()
            print(guess)
            print("You guessed the word!\nYou survived!")
        else:
            print("You lost!")
        break
