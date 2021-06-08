import os
import random
import time

# global variables
selectedNumber = 0
minValue = 1
maxValue = 0
gameCurrentlyActive = True

# general
def clearScreen():
  os.system('cls')
  return

def selectNumber(min, max):
  return random.randint(min, max)

def getInt(string):
  integer = 0
  notDone = True
  while notDone:
    value = input(string)
    try:
      integer = int(value)
    except ValueError:
      print("Please input an integer")
      continue
    notDone = False
  return integer

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

def begin():
  clearScreen()
  global minValue
  global maxValue
  minValue = 1
  maxValue = 0
  while maxValue <= minValue:
    minValue = getInt("State a minimum value: ")
    maxValue = getInt("State a maximum value: ")
    if maxValue <= minValue:
      clearScreen()
      print("Please ensure your minimum value is lower than your maximum value")
  global selectedNumber
  selectedNumber = selectNumber(minValue, maxValue)
  print("Number selected! Are you ready?")
  notReady = True
  while notReady:
    if yesNoLoop():
      notReady = False
    else:
      print("Okay I'll wait")
      time.sleep(5)
      print("Are you ready now?")

def restartGameQuestion():
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

def init():
  clearScreen()
  print("Hewwo uwu")
  print("Would you like to begin?")

  if yesNoLoop():
    begin()
  else:
    endGame()
  return

def update():
  global minValue
  global maxValue
  clearScreen()
  while gameCurrentlyActive:
    print("I am thinking of a number between %s and %s" % (minValue, maxValue))
    guess = getInt("What number do you think that number is? ")
    clearScreen()

    if guess == selectedNumber:
      print("You got it!")
      restartGameQuestion()
    else:
      if guess < selectedNumber:
        if guess < minValue:
          print("%s is lower than the minimum value" % guess)
        else:
          minValue = guess
      else:
        if guess > maxValue:
          print("%s is higher than the maximum value" % guess)
        else:
          maxValue = guess
  return

def exit():
  clearScreen()
  print("Thank you for playing!")
  return

# main
init()
update()
exit()