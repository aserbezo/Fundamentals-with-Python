n = int(input())
water_tank = 255
counter = 0
for i in range(n):
    current = int(input())
    if water_tank - current < 0:
        print("Insufficient capacity!")
    else:
        counter += current
        water_tank -= current

print(counter)
