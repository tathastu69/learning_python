import random
option = ("rock", "paper", "scissor")
player = None
computer = random.choices(option)

player = input("enter the choice (rock, paper, scissor) : ")
print(f"player : { player}")
print(f"computer : {computer}")
