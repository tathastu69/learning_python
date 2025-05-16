#number guessing game 
import random
lowest_num = 1
higehst_num = 100
answer = random.randint(lowest_num, higehst_num)

guesses = 0
is_running = True
print("python number guessing game")
print(f"select a number between {lowest_num} and {higehst_num}")

while is_running:

    guess = input("enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < lowest_num or guess > higehst_num:
            print("the number is out of range")
            print(f" please select a number between {lowest_num} and {higehst_num}")
        elif guess > answer:
            print("too high try again !")
        elif guess < answer:
            print("too low try again !")
        else:
            print(f"correct! the answer was {answer}")
            print(f"number of guesses: {guesses}")
            is_running = False

    else:
        print("invalid guess")
        print(f" please select a number between {lowest_num} and {higehst_num}")
