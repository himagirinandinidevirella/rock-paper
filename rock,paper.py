import random
options = ["rock", "paper", "scissors"]
while True:
    player = input("Enter rock, paper, or scissors: ").lower()
    computer = random.choice(options)
    print("Computer chose:", computer)
    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer == "paper":
        print("You Win!")
    else:
        print("Computer Wins!")
        play_again = input("Play again? (yes/no): ").lower()
    if play_again == "no":
        print("Thank you for playing!")
        break