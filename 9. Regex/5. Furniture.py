import  re

bought = []
total = 0
pattern = r"^>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)$"
command = input()
while command != "Purchase":
      match = re.search(pattern,command)
      if match:
          furniture, price,quantity = match.groups()
          bought.append(furniture)
          total += float(price) * int(quantity)
      command = input()

print("Bought furniture:")
for i in bought:
    print(i)
print(f"Total money spend: {total:.2f}")
# \.? s vurpositelnata moje da ima moje i da nqma tochka