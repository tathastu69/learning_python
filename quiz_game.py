questions = (
    "what is the color of grass ?",
    "what is python ?",
    "Height of Mt.Everest ?",
    "have you ever touched grass ?",
    "what is the color of sun"
)

options = (
    ("a.blue", "b. green", "c.black", "d. haven't touched yet"),
    ("a.snake", "b. animal", "c. bird", "d. insect"),
    ("a. 5ft", "b. infinity", "c. 8848.86m","d. its taller than me"),
    ("a. what is grass", "b. yes", "c. no", "d. eww"),
    ("a. black", "b. white", "c. orange", "d. colorless")
)

answers = ('d', 'a', 'd', 'a', 'c' )

score = 0
guesses = []

for i in range(len(questions)):
    print("-------------------")
    print(f"Q{i + 1} : {questions[i]}")

    for option in options[i]:
        print(option)


    guess = input("enter (a,b,c,d): ").lower()
    while guess not in ['a','b','c','d']:
        print("Invalid input! Please enter (a,b,c,d): ")
        guess = input("Enter your answer (a,b,c,d): ").lower()

    guesses.append(guess)

    if guesses == answers[i]:
        print("correst!")
        score += 1
    else:
        print(f"Incorrect! The correct answer is '{answers[i]}'.")
    
print("------------------")
print("----result----")
print("Correct answers: ", ' '.join(answers))
print("Your guesses:    ", ' '.join(guesses))

score = int(score/len(questions)*100)
print(f"your score is {score}%")