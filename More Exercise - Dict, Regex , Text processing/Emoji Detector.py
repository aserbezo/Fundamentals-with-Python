import re

pattern = r"(::|\*\*)([A-Z][a-z]{2,})\1"

cool_treshold = input()
digits = r"\d"
cools = []
check = re.findall(digits,cool_treshold)
total = 1
for num in check:
    total *= int(num)
print(f"Cool threshold: {total}")
match = re.finditer(pattern,cool_treshold)
emoji_count = 0
for i in match:
  name = i.group(2)
  points = 0
  emoji_count += 1
  for chr in name:
      points += ord(chr)
  if points > total:
     cools.append(i.group(1) + name + i.group(1))

print(f"{emoji_count} emojis found in the text. The cool ones are:")
for i in cools:
    print(i)
