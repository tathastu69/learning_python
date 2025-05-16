import random
option = ("rock", "paper", "scissor")
player = None
computer = random.choices(option)
running = True
while running:
    player = None
    computer = random.choices(option)

    while player not in option:
        player = input("enter the choice (rock, paper, scissor) : ")


    print(f"player : { player}")
    print(f"computer : {computer}")

    if player == computer:
        print("it's a tie ")
    elif player == "rock" and computer == "scissor":
        print("you win !")
    elif player == "paper" and computer == "rock":
        print("you win!")
    elif player == "scissor" and computer ==" paper":
        print("you win")
    else:
        print("you lost")

    play_again = input("play again ?? (y/n): ").lower()
    if play_again !="y":
        running = False

print("thanks for playing! ")