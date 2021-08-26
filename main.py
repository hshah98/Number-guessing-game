from art import logo
from random import randint

random_number = randint(1, 100)
is_game_over = False

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
# print(f"Psst, the correct answer is: {random_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

def play_game(number):
  print(f"You have {attempts} attempt(s) remaining to guess the number.")
  guess = int(input("Make a guess: "))

  if guess < number:
    print("Too low.\nGuess again.")
  elif guess > number:
    print("Too high.\nGuess again.")
  else:
    print(f"You've got it! The correct answer was {number}.")
    return True

while not is_game_over:
  guessed_correctly = play_game(random_number)
  if guessed_correctly:
    is_game_over = True
  attempts -= 1
  if attempts == 0:
    print("You've run out of guesses, you lose.")
    is_game_over = True  
  
