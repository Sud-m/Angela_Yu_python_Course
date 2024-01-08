import random, os
os.system("cls")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts = 10 if difficulty == "easy" else 5
random_number = random.randint(1,100)
while attempts >= 1:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))  
  if guess > random_number:
    print("Too high.")

  elif guess < random_number:
    print("Too low.")
  
  else:
    print(f"You got it! The answer was {random_number}")
    break
  
  attempts -= 1
  if attempts > 0:
    print("Guess again.")
  else:
    print("You've run out of guesses, you lose!") 