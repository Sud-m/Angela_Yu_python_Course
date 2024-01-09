import os
import random
import art


def deal_card():
    return random.choice(list(cards.keys()))


cards = {
    "ace": 11,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "jack": 10,
    "queen": 10,
    "king": 10
}

os.system("cls")
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") != 'n':
    os.system("cls")
    print(art.logo)
    user_cards = []
    computer_cards = []
    usercard1, usercard2 = deal_card(), deal_card()
    computercard1, computercard2 = deal_card(), deal_card()
    user_cards.append(cards[usercard1]), user_cards.append(cards[usercard2])
    computer_cards.append(cards[computercard1]), computer_cards.append(cards[computercard2])
    print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"\tComputer's first card: {computer_cards[0]}")

    while input("Type 'y' to get another card, type 'n' to pass: ") == 'y' and sum(user_cards) <= 21:
        newcard = deal_card()
        user_cards.append(cards[newcard])
        print(f"\tYour cards: {user_cards}, current score: {sum(user_cards)}")
        print(f"\tComputer's first card: {computer_cards[0]}")
        if 11 in user_cards and sum(user_cards) > 21:
            user_cards = [1 if i == 11 else i for i in user_cards]
        if sum(user_cards) > 21:
            print(f"\tYour final hand: {user_cards}, final score: {sum(user_cards)}")
            break
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'n':
            break

    while sum(computer_cards) <= 21:
        newcard = deal_card()
        computer_cards.append(cards[newcard])
        if 11 in computer_cards and sum(computer_cards) > 21:
            computer_cards = [1 if i == 11 else i for i in computer_cards]

    print(f"\tComputer's final hand: {computer_cards}, final score: {sum(computer_cards)}")

    userscore, computerscore = sum(user_cards), sum(computer_cards)

    if userscore > 21 and computerscore > 21:
        print("You went over. You lose! 😤")
        continue

    if userscore == computerscore:
        print("Draw!")
    elif computerscore == 21:
        print("Lose, Computer has Blackjack! 😱")
    elif userscore == 21:
        print("Win with a Blackjack! 😎")
    elif userscore > 21:
        print("You went over, you lose! 😭")
    elif computerscore > 21:
        print("Computer went over. You win! 😁")
    elif userscore > computerscore:
        print("You win! 😃")
    else:
        print("You lose! 😤")
