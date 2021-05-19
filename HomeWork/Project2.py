from random import randint
import time

class HangMan():

  def __init__(self, word):
    self.word = word
    self.correctGuesses = set()
    self.errors = set()
    self.totalCharacters  = set()
    for character in word:
      if character != " ":
        self.totalCharacters.add(character.lower())

  def drawLetters(self):
    # print(self.correctGuesses)
    # print(self.errors)
    # print(self.totalCharacters)
    for character in word:
      if character == " ":
        print(" ", end=" ")
      else:
        if character.lower() in self.correctGuesses:
          print(character, end=" ")
          
        else:
          print("_", end=" ")

  def drawHangMan(self):
    numberOfErrors = len(self.errors)
    print("\n\n")
    for i in range(8):
      if i == 0:
        print("\t ______")

      elif i == 1:
        print("\t|      |")

      elif i == 2:
        if numberOfErrors > 0:
          print("\t|      O")
          numberOfErrors -= 1
        else:
          print("\t|      ")

      elif i == 3:
        if numberOfErrors > 0:
          print("\t|     _|_")
          numberOfErrors -= 1
        else:
          print("\t|      ")

      elif i == 4:
        if numberOfErrors > 0:
          print("\t|    / | \\")
          numberOfErrors -= 1
        else:
          print("\t|      ")
        

      elif i == 5:
        if numberOfErrors > 0:
          print("\t|      |")
          numberOfErrors -= 1
        else:
          print("\t|      ")
        

      elif i == 6:
        if numberOfErrors > 0:
          print("\t|     _|_")
          numberOfErrors -= 1
        else:
          print("\t|      ")
        

      elif i == 7:
        if numberOfErrors > 0:
          print("\t|__  /   \\")
          numberOfErrors -= 1
        else:
          print("\t|__    ")


  def guessCharacter(self, nextGuess):
    if nextGuess.lower() in self.word.lower():
      self.correctGuesses.add(nextGuess.lower())
    else:
      self.errors.add(nextGuess.lower())

    if len(self.errors) >= 6:
      return "Hang Man"
    elif self.totalCharacters.issubset(self.correctGuesses) and len(self.totalCharacters) == len(self.correctGuesses):
      return "Win"
    else:
      return "Continue"


print("Hang Man!")
print("What mode would you like to play")
print("\t1)\tSingle Player")
print("\t2)\tTwo Player")
modeSelection = int(input("Your Choice: "))

if modeSelection == 1:
  print("Selecting a random word.....")
  file = open("words_alpha.txt", "r")
  wordLines = file.readlines()
  randomIndex = randint(0, len(wordLines))
  word = wordLines[randomIndex].strip()
  time.sleep(2)
else:
  word = input("Please enter the word to be guessed: ")


print(chr(27) + "[2J")
hangMan = HangMan(word)

errors = set()
correctGuesses = set()
playerInput = ""
result = "Continue"
while result == "Continue":
  print(chr(27) + "[2J")
  hangMan.drawLetters()
  hangMan.drawHangMan()
  playerInput = input("\n\n\nPlease enter your guess: ")
  if playerInput == "" or playerInput == " " or playerInput in hangMan.correctGuesses:
    continue;
  result = hangMan.guessCharacter(playerInput)

print(result)
print("The Word Was:", word)


#  _____
# |     |
# |     O
# |    _|_
# |   / | \
# |     |
# |    _|_
#_|_  /   \