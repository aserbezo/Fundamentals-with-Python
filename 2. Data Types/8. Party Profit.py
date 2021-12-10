from math import  floor
group_size = int(input())
days_travel = int(input())

total_colins = 0


for day in range(1, days_travel + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5

    if day % 3 == 0:
        total_colins -= group_size * 3
    if day % 5 == 0:
        total_colins += group_size * 20
        if day % 3 == 0:
            total_colins -= group_size * 2
    total_colins += 50
    total_colins -= group_size * 2
coins_per_traverler = floor(total_colins // group_size)
print(f"{group_size} companions received {coins_per_traverler} coins each.")


