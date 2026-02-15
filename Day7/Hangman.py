import random
word_list: list[str] = ["apple", "banana", "cherry", "date", "elderberry"]
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.Then print the chosen_word.
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
    guess = input("Guess a letter: ")



# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")
#TODO-5 :create a "display"that puts the guess letter in the right position and _ in the wrong position
#TODO-7 change the for loop so that you keep the previous guess letter in the display
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

    if "_" not in display:
        game_over = True
        print("You win")
