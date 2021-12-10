budget = float(input())
price_kg_flour = float(input())

# recipe for one bread
# eggss = 1pack
# flour = 1kg
# milk =0.250l

# price of 1 pack eggs  75 %= price 1kg flour
# price  for 1l milk = 25 % more that price of the 1kg flour
# notice that we need 0.250 ml for once bread

price_egg = 0.75 * price_kg_flour
price_milk_1l = price_kg_flour * 1.25 / 4
total_budget = 0
current_count_bread = 0
bread_price = price_egg + price_milk_1l + price_kg_flour
colored_eggs = 0

while budget - bread_price >= 0:
        budget -= bread_price
        current_count_bread += 1
        colored_eggs += 3
        if current_count_bread % 3 == 0:
            colored_eggs -= current_count_bread - 2
print(f"You made {current_count_bread} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")







