from Tools.scripts.nm2def import symbols

start = int(input())
final = int(input())
all = ""

for character in range(start, final + 1):
    all += chr(character) + " "
print(all)