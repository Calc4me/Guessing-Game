import random
import time

# Define Variables
max = 0
# Max number (Depends on difficulty))
diff = ""
# Difficulty
min = 0
#  Minimum number (0)
num = 0
#  Random number
tries = 0
# #of tries (Depends on difficulty)
guess = 0
#Guess
win = False
#Win condition
play = True
#Play condition
numofguesses = 1
# #of gueses in the difficulty (Depends on difficulty)
playagain = ""
# y = play again
# n = don't play again
error = 0
# error:
# 0 = no error
# 1 = input error
# 2 = game end "error"
def GuessingGame():
  print("  _______  ___________________  _______  ________   __  _______")
  print(" / ___/ / / / __/ __/ __/  _/ |/ / ___/ / ___/ _ | /  |/  / __/")
  print("/ (_ / /_/ / _/_\\ \\_\\ \\_/ //    / (_ / / (_ / __ |/ /|_/ / _/")
  print("\\___/\\____/___/___/___/___/_/|_/\\___/  \\___/_/ |_/_/  /_/___/  ")
def easy():
  print("  _____                ")
  print(" | ____|__ _ ___ _   _ ")
  print(" |  _| / _` / __| | | |")
  print(" | |__| (_| \\__ \\ |_| |")
  print(" |_____\\__,_|___/\\__, |")
  print("                 |___/ ")
def medium():
  print("  __  __          _ _                 ")
  print(" |  \\/  | ___  __| (_)_   _ _ __ ___  ")
  print(" | |\\/| |/ _ \\/ _` | | | | | '_ ` _ \\ ")
  print(" | |  | |  __/ (_| | | |_| | | | | | |")
  print(" |_|  |_|\\___|\\__,_|_|\\__,_|_| |_| |_|")
def hard():
  print("  _   _               _ ")
  print(" | | | | __ _ _ __ __| |")
  print(" | |_| |/ _` | '__/ _` |")
  print(" |  _  | (_| | | | (_| |")
  print(" |_| |_|\\__,_|_|  \\__,_|")
def expert():
  print("  _____                      _   ")
  print(" | ____|_  ___ __   ___ _ __| |_ ")
  print(" |  _| \\ \\/ / '_ \\ / _ \\ '__| __|")
  print(" | |___ >  <| |_) |  __/ |  | |_ ")
  print(" |_____/_/\\_\\ .__/ \\___|_|   \\__|")
  print("            |_|                  ")
def ore():
  print("   ___  _ __ ")
  print("  / _ \\| '__|")
  print(" | (_) | |   ")
  print("  \\___/|_|   ")
def custom():
  print("   ____          _                  ")
  print("  / ___|   _ ___| |_ ___  _ __ ___  ")
  print(" | |  | | | / __| __/ _ \\| '_ ` _ \\ ")
  print(" | |__| |_| \\__ \\ || (_) | | | | | |")
  print("  \\____\\__,_|___/\\__\\___/|_| |_| |_|")
  print("__________________________________________________")
  print("")
def bar():
  print("______________________________________________________________")
def winn():
  print(" __   __           __        ___       _ ")
  print(" \\ \\ / /__  _   _  \\ \\      / (_)_ __ | |")
  print("  \\ V / _ \\| | | |  \\ \\ /\\ / /| | '_ \\| |")
  print("   | | (_) | |_| |   \\ V  V / | | | | |_|")
  print("   |_|\\___/ \\__,_|    \\_/\\_/  |_|_| |_(_)")
def large():
  print("")
  print("  _____ ___   ___    _        _    ____   ____ _____ ")
  print(" |_   _/ _ \\ / _ \\  | |      / \\  |  _ \\ / ___| ____|")
  print("   | || | | | | | | | |     / _ \\ | |_) | |  _|  _|  ")
  print("   | || |_| | |_| | | |___ / ___ \\|  _ <| |_| | |___ ")
  print("   |_| \\___/ \\___/  |_____/_/   \\_\\_| \\_\\_____|_____|")
def small():
  print("")
  print("  _                                    _ ")
  print(" | |_ ___   ___    ___ _ __ ___   ___ | |")
  print(" | __/ _ \\ / _ \\  / __| '_ ` _ \\ / _ \\| |")
  print(" | || (_) | (_) | \\__ \\ | | | | | (_) | |")
  print("  \\__\\___/ \\___/  |___/_| |_| |_|\\___/|_|")
def losee():
  print("You lose.")
  print(" __        _ _                ")
  print("/ _|  __ _(_) |_   _ _ __ ___ ")
  print("| |_ / _` | | | | | | '__/ _ \\ ")
  print("|  _| (_| | | | |_| | | |  __/")
  print("|_|  \\__,_|_|_|\\__,_|_|  \\___|")
#Text art

#Intro
GuessingGame()
print("Welcome!")
time.sleep(0.5)
print("This is a guessing game.")
bar()
time.sleep(0.5)

while play is True:
  #Text art intro
  print("Choose your difficulty:")
  time.sleep(0.5)
  easy()
  time.sleep(0.25)
  medium()
  time.sleep(0.25)
  hard()
  time.sleep(0.25)
  expert()
  time.sleep(0.5)
  ore()
  time.sleep(0.25)
  custom()

  #Choose Difficulty
  diff = ""
  print("Guess the number in at most the number of tries provided.")
  while diff not in ["easy", "medium", "hard", "expert", "yes", "custom"]:
    diff = input("What difficulty? Please enter the name with good spelling. ").lower()
    if diff not in ["easy", "medium", "hard", "expert", "yes", "custom"]:
      print("Invalid difficulty. Please try again.")

  #Define the max and guesses
  if diff == "easy":
    min = 0
    max = 10
    tries = 4
    num = random.randint(min, max)
  elif diff == "medium":
    min = 0
    max = 25
    tries = 7
    num = random.randint(min, max)
  elif diff == "hard":
    min = 0
    max = 50
    tries = 9
    num = random.randint(min, max)
  elif diff == "expert":
    min = 0
    max = 200
    tries = 10
    num = random.randint(min, max)
  elif diff == "yes":
    min = 0
    max = 1000
    tries = 21
    num = random.randint(min, max)
  elif diff == "custom":
    min = int(input("Enter the minimum number: "))
    max = int(input("Enter the maximum number: "))
    tries = int(input("Enter the number of tries: "))
    num = random.randint(min, max)

  #Introduce difficulty
  print("Difficulty:")
  print(diff)
  print("")
  print("Minimum number: " + str(min))
  print("")
  print("Maximum number: " + str(max))
  print("")
  print("Tries: " + str(tries))
  bar()
  print("")

  #Main loop
  win = False
  while tries > 0:
    print("")
    print("")
    print("This is guess " + str(numofguesses) + ", with " + str(tries) + " tries left.")
    print("")
    #Guess loop
    guess = input("What is your guess? ")
    while int(guess) < min or int(guess) > max:
      print("Try again. Out of range.")
      guess = input("What is your guess? ")
    guess = int(guess)
    #Check if guess is correct
    if guess == num:
      print("")
      print("That's right!")
      time.sleep(0.5)
      winn()
      bar()
      print("")
      print("")
      print("It took you " + str(numofguesses) + " guesses.")
      win = True
      break
    elif guess > num:
      large()
      bar()
    elif guess < num:
      small()
      bar()
    #Update variables
    tries = tries - 1
    numofguesses += 1
    print("")

  #Loss condition
  if win is False:
    losee()
    print("It was " + str(num) + ".")

  #Play Again
  playagain = ""
  error = 2
  while playagain != "y" and playagain != "n":
    playagain = input("Play again? (y/n) ").lower()
    if playagain != "y" and playagain != "n":
      print("Invalid Input")
  if playagain == "n":
    play = False
    print("Thanks for playing!")
    break