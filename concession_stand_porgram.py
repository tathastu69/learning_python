menu = {"pizza":4.99, 
        "soda":3.40,
        "burger":5.00,
        "chips":4.80}

cart = []
total = 0

print(f"-----menu-----")
for key, value in menu.items():
    print(f"{key:10} is {value:2}")
print("--------------")
while True:
    food = input("select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get (food) is not None:
                cart.append(food)

print("-----your order-----")
total = 0
for food in cart:
    total += menu.get(food)
    print(food, end=" ")



print()

print(f"your total is {total}")