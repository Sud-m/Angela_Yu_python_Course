import os
import art
bids={}
print(art.logo)
while True:
  name=input("What is your name?: ")
  bid=int(input("What is your bid? : $"))
  bids[name]=bid
  if input("Are there any other bidders? Type 'yes' or 'no'.").lower() == "no":
    break
  os.system("cls")
max=0
winner=""
for key in bids:
  if bids[key]>max:
    max=bids[key]
    winner=key

print(f"The winner is {winner} with a bid of ${bids[winner]}")