import re

pattern = r"%([A-Z][a-z]+)%.*<([\w]+)>.*\|(\d+)\|.*?(\d+\.?\d*)\$"

text = input()
total = 0
while text != "end of shift":
    match = re.search(pattern,text)
    if match:
           customer,product,count,price = match.groups()
           cost = int(count) * float(price)
           print(f"{customer}: {product} - {cost:.2f}")
           total += cost

    text = input()

print(f"Total income: {total:.2f}")