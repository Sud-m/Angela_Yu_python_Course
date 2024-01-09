import random
import os
from game_data import data
from art import logo, vs




def random_account():
  return random.choice(data)

def format(person):
  person_name = person["name"]
  person_description = person["description"]
  person_country = person["country"]
  return f"{person_name}, a {person_description}, from {person_country}"

def guess_checker(account1, account2, guess):
  a1_followers, a2_followers = account1["follower_count"], account2["follower_count"]
  if guess=='A':
    return a1_followers > a2_followers
  else:
    return a2_followers > a1_followers

def game():
  right_guess = True
  final_score = 0
  randaccount1, randaccount2 = random_account(), random_account()
  
  while right_guess:
    while randaccount1 == randaccount2:
      randaccount2 = random_account()
    os.system("cls")  
    print(logo)
    if final_score > 0:
      print(f"You're right! Current score: {final_score}")
    print(f"Compare A: {format(randaccount1)}.")
    print(vs)
    print(f"Against B: {format(randaccount2)}.")
    
    userguess = input("Who has more followers? Type 'A' or 'B': ")

    if guess_checker(account1 = randaccount1, account2 = randaccount2, guess = userguess) == True:
      final_score += 1
      if userguess == 'B':
        randaccount1 = randaccount2
      randaccount2 = random_account()
        
    else:
      print(f"Sorry, that's wrong. Final score: {final_score}")
      right_guess = False

game()