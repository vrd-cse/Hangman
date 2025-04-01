import random
from hangman_art import stages
from hangman_word import word_list
from hangman_art import logo

print(logo)
lives = 6
#  chosing a random word-->

chosen_word = random.choice(word_list)

placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print("Word to guess : "+ placeholder)

game_over = False    
correct_letter = []

# taking inputs from player-->

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter :").lower()
    
    if guess in correct_letter:
        print("you have already guessed letter")
    
    display = ""
    
    for letter in chosen_word:
        
        if letter ==guess :
            display += "_"
            correct_letter.append(guess)
        elif letter in correct_letter :
            display += letter         
        else:
            display += "_"
        
    if guess not in chosen_word:
        lives -= 1 
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        if lives ==0 :
            game_over = True
            print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    print(stages[lives])