import random
from hangman_words import word_list
from hangman_art import stages, logo

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.Then print the chosen_word.
#word_list: list[str] = ["apple", "banana", "cherry", "date", "elderberry"]
#TODO-11 update the word_list to use the 'word_list' from hangman_words.py
#TODO-8- Create a variable called 'lives' to keep track of the number of lives left. 
lives: int = 6
#TODO-13-import the logo from hangman_art.py and print it at the start of the game.
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-4 - Create a placeholder with the same length as the chosen_word and fill it with "_"
word_length: int = len(chosen_word)
placeholder: str = ""
for position in range(word_length):
    placeholder += "_"
print(placeholder)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#TODO-6 - use the while loop to let the user guess again
game_over: bool = False
correct_letters: list[str] = []
while not game_over:
    #TODO-17-update the code below to tell the user how many lives they have left 
    print(f"*****************************{lives} lives left*****************************")
    guess = input("Guess a letter: ")



# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
#TODO-5 :create a "display"that puts the guess letter in the right position and _ in the wrong position
#TODO-7 change the for loop so that you keep the previous guess letter in the display
#TODO-15-if the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in correct_letters:
        print(f"You've already guessed {guess}")
    
    display:str= ""
    for letter in chosen_word:
        if letter == guess:
            display+=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_"
    print(display)

#TODO-9 - If guess is not a letter in the chosen_word, reduce 'lives' by 1.
#If lives goes down to 0 then the game should stop and it should print "You lose."
#TODO-16-if the letter is not in the chosen_word, print the letter and let them know it's not in the word.
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed{guess} that is not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            #TODO-18-update the code below to print "You lose." if the user has no lives left.
            print(f"*********It was {chosen_word}. You lose*********")


    if "_" not in display:
        game_over = True
        #TODO-19-update the code below to print "You win."
        print("*********You win*********")
#TODO-10 - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#TODO-14-update the code below to use stage list from the file hangman_art.py
    print(stages[lives])