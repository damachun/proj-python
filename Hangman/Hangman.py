import os
import random

# global variables
wordOptions = []
word = ""
currentWord = ""
guesses = []
gameCurrentlyActive = True
maxChances = 10
chances = maxChances

# general
def clearScreen():
  os.system('cls')
  return

def initText():
  textFile = open("WordList.txt", "r")
  return textFile.readlines()

def selectIndex(wordOps):
  # remove selected word from list
  return random.randint(0, len(wordOps) - 1)

def yesNoLoop():
  notDone = True
  while notDone:
    option = input("'Y' for yes, 'N' for no: ")
    if option == 'Y' or option == 'y':
      return True
    else:
      if option == 'N' or option == 'n':
        return False
      else:
        print("Please input either 'Y' or 'N'")
  return

# game specific
def begin():
  clearScreen()
  print("Let's begin!")
  global chances
  chances = maxChances
  global guesses
  guesses.clear()
  global word
  global wordOptions
  word = wordOptions.pop(selectIndex(wordOptions))
  global currentWord
  currentWord = "_ " * len(word)
  return

def letterCheck(upperCase, lowerCase):
  if upperCase in word or lowerCase in word:
    global currentWord
    tempWord = ""
    for index in range(len(word)):
      if upperCase == word[index]:
          tempWord += upperCase
      else:
        if lowerCase == word[index]:
            tempWord += lowerCase
        else:
            tempWord += currentWord[index * 2]
      tempWord += " "
    currentWord = tempWord

    if "_" not in currentWord:
      clearScreen()
      print("You won! The word was '%s'" % word)
      restartGameQuestion()
    else:
      print("You got one!")

  else:
    global chances
    chances -= 1
    if chances <= 0:
      clearScreen()
      print("You lost! The word was '%s'" % word)
      restartGameQuestion()
  return

def restartGameQuestion():
  if len(wordOptions) == 0:
    print("You have cleared the entire word list.")
    print("Please get a life.")
    input("Press any key to exit the game.")
    endGame()
    return

  print("Restart the game?")
  if yesNoLoop():
      begin()
  else:
    endGame()
  return

def endGame():
  global gameCurrentlyActive
  gameCurrentlyActive = False
  return

# core

def init():
  clearScreen()
  print("Hewwo uwu")
  print("Would you like to begin?")

  if yesNoLoop():
    tempWordOptions = initText()
    global wordOptions
    for wordOp in tempWordOptions:
      wordOptions.append(wordOp.rstrip())
    begin()
  else:
    endGame()
  return

def update():
  global guesses
  global currentWord
  global word

  while gameCurrentlyActive:
    if chances < maxChances:
      print("You have %s chances left" % chances)
      print("Guesses: %s" % guesses)
    print(currentWord)
    option = input("Guess a letter: ")

    upperCase = option.upper()
    lowerCase = option.lower()

    if upperCase in guesses or lowerCase in guesses:
      clearScreen()
      print("You have guessed %s before." % option)
      continue
    guesses.append(option)

    letterCheck(upperCase, lowerCase)
      
    clearScreen()

  return

def exit():
  clearScreen()
  print("Thank you for playing!")
  return

# main

init()
update()
exit()