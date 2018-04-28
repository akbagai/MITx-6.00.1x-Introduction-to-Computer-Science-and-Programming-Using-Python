# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    uniqueChar = set(secretWord)
    def matchAllChar(s, lettersGuessed):
        # base
        n = len(s)
        if n == 1:
            c = next(iter(s))
            if c in lettersGuessed:
                return True
            else:
                return False
        else:
            return matchAllChar(set(s.pop()), lettersGuessed) and matchAllChar(s, lettersGuessed)
    return matchAllChar(uniqueChar, lettersGuessed)

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's','l','a']
#print(isWordGuessed(secretWord, lettersGuessed))


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    if len(secretWord) == 1:
        if secretWord in lettersGuessed:
            return secretWord
        else:
            return "_"
    else:
        return getGuessedWord(secretWord[0], lettersGuessed) + getGuessedWord(secretWord[1:], lettersGuessed)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alpha = string.ascii_lowercase
    for c in lettersGuessed:
        alpha = alpha.replace(c, '')
    return alpha

def saveGuess(letter, lettersGuessed):
        '''
        Save letter entered by user.   If the save is successful, return True.
        If the letter is already saved, return False
        :param letter: letter to to saved
        :param lettersGuessed: list of saved letters
        :return: True if save is successful, False if letter was already saved previously.
        '''
        if letter in lettersGuessed:
            return False
        else:
            lettersGuessed.append(letter)
            return True
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guesses_left = 8
    lettersGuessed = []
    guessedWord = ""
    game_won = False

    print("Welcome to the game, Hangman!")
    #print("Secret: {}".format(secretWord))
    print("I am thinking of a word that is {} letters long.".format(len(secretWord)))

    # Game loop
    while guesses_left > 0:
        print("-------------")
        print("You have {} guesses left".format(guesses_left))
        print("Available letters: {}".format(getAvailableLetters(lettersGuessed)))
        user_input = input('Please guess a letter: ')
        letter = user_input.lower()

        if saveGuess(letter, lettersGuessed):
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            if letter in secretWord:
                print("Good guess: {}".format(guessedWord))
            else:
                guesses_left -= 1
                print("Oops! That letter is not in my word: {}".format(guessedWord))
            if isWordGuessed(secretWord, lettersGuessed):
                game_won = True
                break
        else:
            print("Oops! You've already guessed that letter: {}".format(guessedWord))

    print("-------------")
    if game_won:
            print("Congratulations, you won!")
    else:
            print("Sorry, you ran out of guesses. The word was {}.".format(secretWord))





#wordlist = loadWords()
hangman(chooseWord(wordlist))








# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
