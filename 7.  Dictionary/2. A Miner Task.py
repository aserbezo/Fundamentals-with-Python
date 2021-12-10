command = input()
resources = {}

while command != "stop":
    if command not in resources:
        resources[command] = 0
    qty = int(input())
    resources[command] += qty

    command = input()


[print(f'{key} -> {value}') for key, value in resources.items()]