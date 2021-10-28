#Importing random module for later function
import random

#Setting a single word for initial build ^will add randomeness later
random_word = 'dice'
#putts the chosen word into a list
letters = list(random_word)


game_end_flag = False




#this function prints the entirty of words.txt will randomize from this list
# with open("words.txt") as words:
#     print(words.read())

#user will choose to play the game
user_input = input('Would you like to play Mystery Word?: ')
letter_guess = str(user_input)

#function begins game and sets difficulty level
while user_input != 'Quit' and game_end_flag == False:
    if user_input == 'Yes':
        user_input = input('Would you like to play Easy, Normal, or Hard?: ')

        if user_input == 'Easy':
            print('You have chosen an easy word!')
            print(f'There are {len(random_word)} letters in the word.')
            user_input = input('Choose your letter!: ')

            if user_input in random_word:
                print('You found one! ')

            elif user_input not in random_word:
                user_input = input("You are incorrect! Choose your next letter. ")

            


        # elif user_input == 'Normal':
        #     print('You have chosen a normal word!')
            
        # elif user_input == 'Hard':
        #     print('You have chosen a hard word!')
            

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
