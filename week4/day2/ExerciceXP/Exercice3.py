basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
print(basket)

print("...")
basket.remove("Blueberries")
print(basket)

print("...")
basket.insert(2,"kiwi")
print(basket)

print("...")
basket.insert(0,"Apples")
print(basket)

print("...")
count = basket.count("Apples")
print(count)

print("...")
basket.clear()
print(basket)
