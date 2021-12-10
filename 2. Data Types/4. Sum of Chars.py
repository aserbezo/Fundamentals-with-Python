
n = int(input())
sum_ascii = 0

for i in range(n):
    character = input()
    sum_ascii += ord(character)
print(f"The sum equals: {sum_ascii}")
