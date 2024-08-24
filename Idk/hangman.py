# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. 
    Words are strings of lowercase letters.

    Depending on the size of the word list, 
    this function may take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct = 0
    for i in secret_word:
        if i in letters_guessed:
            correct += 1
    
    return correct == len(secret_word)


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word_progress = list(secret_word)
    for i in range(len(word_progress)):
        if word_progress[i] not in letters_guessed:
            word_progress[i] = "*"
    return "".join(word_progress)

        

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    a = list(string.ascii_lowercase)
    for i in letters_guessed:
        a.remove(i)
    a.sort()
    a = "".join(a)
    # For some reason produces an error
    return a



def hangman(secret_word, with_help):
    """
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print(f'the word has {len(secret_word)} letters, you have 10 guesses')
    if with_help: print('If you need help, you can write "!" to reveal a letter at the cost of 3 guesses')
    guesses = 10
    letters_guessed = []
    while guesses > 0:
        if guesses <10 or len(letters_guessed)>1:
            print(f'You have {guesses} guesses left for {len(secret_word) - len(letters_guessed)} letters')
            
        guess = input('make a guess:')
        if guess == '!' and with_help == True:
            if guesses <3:
                print("you don't have enough guesses!")
            else:
                for i in range(len(secret_word)):
                    x = random.choice(secret_word)
                    if x not in letters_guessed: 
                        letters_guessed += x
                        break
                
        elif guess not in string.ascii_lowercase or len(guess)>1:
            print('invalid guess, try again')
        
        elif guess in secret_word:
            print("that's right!")
            letters_guessed += guess
            guesses - 1 
        elif guess not in secret_word:
            print("Wrong!")
            if guess in "aeiou":
                guesses -= 2
            else: 
                guesses -= 1
        if has_player_won(secret_word, letters_guessed):
            print("Congratulations! you have won!")
            break
        print("-----------")
        print("-----------")
        print("-----------")
        print(f"you have not guessed this letters yet: {get_available_letters(letters_guessed)}  ")
        print(f"this is your progress so far: {get_word_progress(secret_word,letters_guessed)}")
    if guesses ==0: print("Loser!")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = 'pa' #choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

