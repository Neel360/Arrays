basket_1 = {"bread", "milk", "eggs", "cheese"," apples","butter","carrots"}
basket_2 = {"bread", "milk", "eggs", "cheese"," oranges","flour","jam"}

print(f"Items in basket 1: {basket_1}")
print(f"Items in basket 2: {basket_2}")

basket_2.add("yogurt")
print(f"Items in basket 2 after adding yogurt: {basket_2}")

common_items = basket_1.intersection(basket_2)
print(f"Common items in both baskets: {common_items}")

all_fruits = basket_1.union(basket_2)
print(f"All items in both baskets: {all_fruits}")

only_basket_1 = basket_1.difference(basket_2)
print(f"Items only in basket 1: {only_basket_1}")

only_basket_2 = basket_2.difference(basket_1)
print(f"Items only in basket 2: {only_basket_2}")

import array as arr
items_prices = arr.array('f', [1.5, 2.0, 3.0, 4.5, 0.5])
print("Prices of items in basket 1: ", items_prices)

items_prices.insert(2, 3)
items_prices.append(2.0)
print("Updated prices of items in basket 1: ", items_prices)

count_of_items = items_prices.count(2.0)
print(f"Count of items with price 2.0: {count_of_items}")

items_prices.reverse()
print("Reversed prices of items in basket 1: ", items_prices)

