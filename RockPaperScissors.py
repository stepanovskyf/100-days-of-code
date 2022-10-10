start = input("What do you choose? Rock, Paper or Scissor\n")
import random
computer = random.randint(0,2)
if (computer == 0):
    computer = "Rock"
elif(computer == 1):
    computer = "Paper"
else:
    computer = "Scissors"
print(computer)
if (start == computer):
    print("Draw")
elif(start == "Rock" and computer == "Paper"):
    print("You lose")
elif(start == "Rock" and computer == "Scissors"):
    print("You win")
elif(start == "Paper" and computer == "Scissors"):
    print("You lose")
elif(start == "Paper" and computer == "Rock"):
    print("You win")
elif(start == "Scissors" and computer == "Paper"):
    print("You win")
elif(start == "Scissors" and computer == "Rock"):
    print("You lose")
else:
    print("You made a mistake")
