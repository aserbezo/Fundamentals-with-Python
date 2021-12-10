from math import  pow

n = int(input())
value_snowball = 0
max_snowball_weight = 0
max_snowball_time = 0
max_snowball_quality = 0

for i in range(n):
    weight_snowball = int(input())
    time_snowball = int(input())
    quality_snowball = int(input())
    current_snowball = pow(weight_snowball / time_snowball , quality_snowball)
    if current_snowball > value_snowball:
        value_snowball = current_snowball
        max_snowball_weight = weight_snowball
        max_snowball_time = time_snowball
        max_snowball_quality = quality_snowball

print(f"{max_snowball_weight} : {max_snowball_time} = {int(value_snowball)} ({max_snowball_quality})")


