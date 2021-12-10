
items_prices = input().split("|")
budget = float(input())
total_budget = budget
list_item_new_prices = []
profit = 0
price_all = 0
new_budget = 0
final =  []

for i in items_prices:
    new_split = i.split("->")
    type_item = new_split[0]
    price = float(new_split[1])
    if budget < price:
        continue
    if type_item == "Clothes":
        if price <= 50.00:
            budget -= price
            list_item_new_prices.append(price)
    elif type_item == "Shoes":
        if price <= 35.00:
            budget -= price
            list_item_new_prices.append(price)
    elif type_item == "Accessories":
        if price <= 20.50:
            budget -= price
            list_item_new_prices.append(price)

for i in list_item_new_prices:
    new_price =(i * 0.4) + i
    price_all += new_price
    profit = (price_all - total_budget) + budget
    new_budget = budget + price_all
    final.append(new_price)

for i in final:
    print(f"{i:.2f}",end=" ")



if new_budget >= 150:
    print(f"\nProfit: {profit:.2f}")
    print("Hello, France!")
else:
    print(f"\nProfit: {profit:.2f}")
    print("Not enough money.")
