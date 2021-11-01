#Importing random module for later function
import random

#Setting a single word for initial build ^will add randomeness later
random_word = 'dice'

#this function will call a random word from the list! WORKS!!!
# with open("words.txt") as words:
#     lines = random.choice(words.readlines())
#     print(lines)

#putts the chosen word into a list
letters = list(random_word)

game_end_flag = False
#Moved this inside def while loop
guess_count= 1
tries_left= 8 - guess_count

#this function prints the entirty of words.txt will randomize from this list
# with open("words.txt") as words:
#     print(words.read())


#I think this will be used to store the guessed letters? 
letter_guess = []

# letter_guess.append(user_input)

#function begins game and sets difficulty level

#user will choose to play the game
user_input = input('Would you like to play Mystery Word?: ')
while user_input != 'Quit' and game_end_flag == False:
    if guess_count == 9:
        print('You have run out of tries!')  
        user_input = input('Would you like to play again? Yes or Quit: ')
        game_end_flag = True
    if user_input == 'Yes':
        user_input = input('Would you like to play Easy, Normal, or Hard?: ')
        if user_input == 'Easy':
            print('You have chosen an easy word!')
                #This will state how many letters are in the word


            print(f'There are {len(random_word)} letters in the word.')

            user_input = input('Choose your letter!: ')
            
            while user_input in random_word:
                #This will add to total attempts, add to used letter list
                #This will also disply number of tries left 
                # letter_guess.append(user_input)
                guess_count += 1
                display = '_' * len(random_word)
                new_display = ''
                
                for r, d in zip(random_word, display):
                    if user_input.lower() == r:
                        new_display += user_input.lower()
                    else:
                        new_display += d
                display = new_display
                print(display)
                # print(random_word.index(user_input))
                print(f'You found one! You have {tries_left} tries remaining.')
                elif user_input not in random_word:
                guess_count += 1
                user_input = input(f"You are incorrect! You have {tries_left} tries remaining. Choose your next letter. ")
easy ()



            
# for letter in random_word:
#     [0,1,2,3]
            
#Build for end of game response
        #        elif user_input == random_number:
        # print('You got it right!')
        # print(f"It took you {guess_count} guesses!")
        # game_end_flag = True

#function will start game in  easy, normal, or hard version
# def 
# while user_input == 'Easy': 
#     user_input = input('Choose your letter!: ')
#         if user_input == True:
#             print('You are correct!: ')
#         print(letter_guess)


# This function will trigger the end of the game
# else if user_input == random_word:
#     Print('You Win!')
#     game_end_flag == True

    # elif user_input == 'Normal':

    # elif user_input == 'Hard':        







# from random import sample
# with open("words.txt") as word_list:
