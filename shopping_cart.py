#shopping cart program

products = []
prices = []
total = 0

while True:
    product = input("enter the product to buy (Q tp quit) : ")
    if product.lower() == "q":
        break
    else:
        price = float(input(f" Enter the price of {product}:$"))
        products.append(product)
        prices.append(price)
        print()

print("----- Your Cart -----")
for product, price in zip(products, prices):
    print(f"{product} - ${price}")

total = sum(prices)
print(f"your total is ${total}")        

