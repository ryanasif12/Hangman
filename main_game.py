import random
from Hangman_art import Stages, logo
from list_of_words_hangman import words

lives = 6
print(logo)

Choosen_word = random.choice(words)

# print(Choosen_word)

#step 4: Create an empty list as place holder and put each letter in that placeholder make sure if your letter length is 3 like bat your place holder length should be 3
# place_holder = ""
# word_length = len(Choosen_word)
# for position in range(word_length):
#     place_holder += "-"
# print(place_holder)

# Step 2: Ask to the user guess a letter and assign that letter to guess_variable and make it lowercase
correct_letter = []
game_over = False
while not game_over:
    print(f"*************************{lives}/6 LEFT LIVES😐😪************************")
    Guess_letter = input("Enter a Guess_letter🧐: ").lower()
      
#Step:3 and 5 Check if the user guess letter is one
#of the letter choosen word from word_list print right 
#other wise wrong and in five step we have creat empty string as dsiplay 
#and store guse letter in that and esle it replace with -
    display = ""
    for letter in Choosen_word:
        if letter == Guess_letter:
            display += letter           
            correct_letter.append(Guess_letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "-" 
    print("Word to Guess",display)
    
    if Guess_letter in correct_letter:
        print(f"You've already Guessed {Guess_letter}")
        
    if Guess_letter not in Choosen_word:
        lives -= 1
        print(f"You Gussed {Guess_letter}, that's not in the word. You lose life.")
        if lives == 0:
            game_over = True
            print(f"*****************It was {Choosen_word}! YOU LOSE😢😢***************") 

    if ("-" not in display):
            game_over = True
            print(f"***************************YOU WIN👏****************************")
    print(Stages[lives])