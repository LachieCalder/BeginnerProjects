#simple game of hangman
import random

#chooses random word from predetermined list
def getWord(words):
    index = random.randrange(0,len(words) - 1)
    return words[index]
    
    
#prints out contents of a list element by element
def printList(list):
    for entry in list:
        print(entry, end=' ')

#gets a single letter guess from player
def getGuess():
    global guessedLetters
    guess = str(input("Guess a letter: "))
    guessedLetters.append(guess) #appends letter guessed to list of letters already guessed
    return guess
    
#checks if guess matches a letter in secret word
def checkList(guessed, secretWord, guess):
    index = 0
    while index < len(secretWord):
        if guess == secretWord[index]:
            guessed[index] = guess
        index = index + 1

#prints results of game
def printResult(guessed, secretWord, attempts):
    print("Guessed so far")
    printList(guessed)    
    print('')
    print("The word was", end=' ')
    printList(secretWord)
    print(". You guessed it in", attempts, "attempts.")

#checks if the guessed word matches secret word
def checkFinished(guessed):
    for entry in guessed:
        if entry == '_':
            return False
    return True

#prints out ascii art of current hangman stage    
def printHangman(stage):
    if stage == 0:
        print("")

    if stage == 1:
        print("___")

    if stage == 2:
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 3:
        print(" _____")
        print(" | ")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 4:
        print(" _____")
        print(" |   |")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 5:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 6:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |   |")
        print(" | ")
        print("_|_")

    if stage == 7:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|")
        print(" | ")
        print("_|_")

    if stage == 8:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" | ")
        print("_|_")

    if stage == 9:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  /")
        print("_|_")

    if stage == 10:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  / \\")
        print("_|_")


words = ['dog', 'cat', 'scissors','unicorn', 'bicycle', 'computer', 'word']
secretWord = getWord(words)
attempts = 0
guessedLetters = []
stage = 0	
#generates a list filled with '_' same length as word
guessed = list('_' * len(secretWord))


while checkFinished(guessed) == False:
    printHangman(stage)
    print("Guessed so far:")
    printList(guessed)
    print(' ')
    print("Letters guessed: ", end='')
    printList(guessedLetters)
    print(' ')
    guess = getGuess()
    checkList(guessed, secretWord, guess)
    attempts = attempts + 1
    if not guess in secretWord:
        stage = stage + 1
    if stage == 10 or checkFinished == True:
        endMessage(secretWord, attempts, guessed)

if stage == 10:
    printHangman(10)
    print("You were hung! The secret word was", end=' ')
    printList(secretWord)
else:
    printResult(guessed, secretWord, attempts)
        
    
    
        
		



