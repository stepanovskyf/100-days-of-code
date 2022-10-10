import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#HINT: You can call clear() to clear the output in the console.
name_and_bid = {}
check = True
while check == True:

    name = input("What is your name? ")
    bid = input("What is your bid? $")
    name_and_bid[name] = bid
    more = input("Are there more people bidding? y/n ")
    if more == "y":
        check = True
    elif more == "n":
        check = False
    cls()
print(max(name_and_bid, key=name_and_bid.get) + f" with bid of ${name_and_bid[max(name_and_bid, key=name_and_bid.get)]}")
input("Press enter to close")