import random


player_name= input("Enter your name: ")
print(f"Welcome {player_name} to the rock, paper and scissor game\n")
choice = ["rock", "paper", "scissors"]
def main():
 computer = random.choice(choice)
 print("Rules of the game: \nrock vs scissors = scissor wins. \npaper vs scissors = scissors wins. \nrock vs paper = paper wins. \npaper vs rock = rock wins")
 player = input("Your choice: ").lower()
 print("Computer chose: " , computer)

 if player == computer:
    print("It is a draw, no winner!")
 elif player == "rock" and computer == "paper":
    print("Computer Wins!")
 elif player == "rock" and computer == "scissors":
    print("Computer wins!")
 elif player == "scissors" and computer == "paper":
    print("Computer wins!")
 elif player == "scissors" and computer == " rock":
    print("You win!")
 elif player == "paper" and computer == "rock":
    print("You win!")
 elif player == "paper" and computer == "scissors":
    print("You win!")
 else:
    print("Choose either paper, rock or scissor")

main()

