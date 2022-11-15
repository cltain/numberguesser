import random
def low(count, guess):
  if count != 1:
    print("Too low.\nGuess again.")
  else:
    print("You have run out of tries :(")
    

def high(count, guess):
  if count != 0:
    print("Too high.\Guess again.")
  else:
    print("You have run out of tries :(")
  
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
num = random.randint(1,100)
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "easy":
  count = 10
  while count > 0:
    guess = int(input(f"You have {count} attempts remaining to guess the number.\nMake a guess. "))
    if guess < num:
      low(count, guess)
      count -= 1
    elif guess > num:
      high(count, guess)
      count -= 1
    elif guess == num:
      print("You guessed the number!")
      break
elif mode == "hard":
  count = 5
  while count > 0:
    guess = int(input(f"You have {count} attempts remaining to guess the number.\nMake a guess. "))
    if guess > num:
      high(count, guess)
      count -= 1
    elif guess < num:
      low(count, guess)
      count -= 1
    elif guess == num:
      print("You guessed the number!") 
      break
