sequance_numbers = input().split()
time_left_car = 0
time_right_car = 0

for i in range(len(sequance_numbers)):
    sequance_numbers[i] = int(sequance_numbers[i])

for i in sequance_numbers:
    middle = (len(sequance_numbers) // 2)
    left_car = sequance_numbers[0:middle]
    right_car = sequance_numbers[middle + 1 ::]

for j in left_car:
    time_left_car += j
    if j == 0:
        time_left_car *= 0.8

for k in range(len(right_car) -1,-1, -1):
    if not  right_car[k]  == 0:
        time_right_car += right_car[k]
    else:
        reduce_speed = time_right_car * 0.2
        time_right_car -= reduce_speed



if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")

else:
    print(f"The winner is right with total time: {time_right_car:.1f}")
