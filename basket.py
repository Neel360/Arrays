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