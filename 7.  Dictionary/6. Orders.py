
command = input().split()
products = {}
while command[0] != "buy":
    product_name = command[0]
    price = float(command[1])
    quatity = int(command[2])
    if product_name not in products:
        products[product_name] = []
        products[product_name].append(price)
        products[product_name].append(quatity)
    else:
        if product_name in products:
            products[product_name].pop(0)
            products[product_name].insert(0, price)
            qty =  products[product_name].pop(1)
            products[product_name].append(qty + quatity)


    command = input().split()


for key , value  in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
