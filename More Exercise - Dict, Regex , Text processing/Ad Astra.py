import  math
import re

pattern = r"(#|\|)([A-Za-z\s]+)\1((\d{0,2}/\d{0,2}/\d{0,2}))\1(\d+)\1"

text = input()

match = re.finditer(pattern,text)
top_calories = 0

for el in match:
    calories = int(el.group(5))
    top_calories += calories
print(f"You have food to last you for: {math.floor(top_calories / 2000)} days!")

match = re.finditer(pattern,text)
for tl in match:
    print(f"Item: {tl.group(2)}, Best before: {tl.group(4)}, Nutrition: {tl.group(5)}")

