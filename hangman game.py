from wordslist import words
import random
# print("\u25cb \u0305") 
# ○ ̅

#dict of key():
hangman_art = {0: ("            ",
                   "            ",
                   "            "),
               1: ("         ○  ",
                   "            ",
                   "            "),
               2: ("         ○  ",
                   "         |  ",
                   "            "),
               3: ("         ○  ",
                   "        ̅ |  ",
                   "            "),
               4: ("         ○  ",
                   "        ̅ |̅  ",
                   "            "),
               5: ("         ○  ",
                   "        ̅ |̅  ",
                   "        /   "),
               6: ("         ○  ",
                   "        ̅ |̅  ",
                   "        / \\")} #\\ to avoid error of using back-slash

def display_man(wrong_guesses):
    print("____________________")
    for line in hangman_art[wrong_guesses]:
        print(line) 
    print("____________________")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words) 
    hint = ["_"] * len(answer)
    wrong_guesses = 0 
    guessed_letters = set()
    is_running =  True #switch to False when game ends
    
    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        # display_answer(answer)
        guess = input("Enter a letter: ").lower()

        # if guess.isnumeric() == True: #OR if guess.isalpha() == False: OR if not guess.isalpha():
        if guess.isalpha() == False: #preferrable 
            print("ONLY INPUT ALBHABETS.")
            continue
        if len(guess) != 1:
            print("ONLY ENTER ONE ALBHABET AT A TIME.")
            continue 
        
        #skip if right guess is repeated
        if guess in guessed_letters:
            print(f"{guess} is already guessed!")
            continue 
        guessed_letters.add(guess)

        if guess in answer: 
            for i in range(len(answer)): #loops the no. of times of len of answer
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            print("The word was: ", answer)
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer) 
            print("YOU LOSE!")
            print("The word was: ", answer)
            is_running = False

    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again == "y":
            main()  # Restart the game by calling the main() fn
        elif play_again == "n":
            print("Thanks for playing!")
            exit()  # Exit the program
        else:
            print("Invalid choice! Only enter 'y' for Yes or 'n' for No.")
        print("Thanks for playing!")
   
if __name__ == "__main__":
    main() 
'''to ensure that the script runs only when executed directly, 
not when imported as a module in another script.'''
    
