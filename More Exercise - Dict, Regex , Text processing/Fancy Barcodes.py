import re

pattern = r"(@#+)([A-Z][A-Za-z\d]{4,}[A-Z])\1"

n = int(input())

for _ in range(n):
    check = input()
    name = re.finditer(pattern, check)
    if name:
        print(name)

    else:
        print("Invalid barcode")



















    #
    # if name:
    #     check_name = name.group()
    #     numbers = [int(el) for el in re.findall(r"\d", check_name)]
    #     if len(numbers) == 0:
    #         numbers = "00"
    #         print(f"Product group: {numbers}")
    #     else:
    #         digits = ""
    #         for i in numbers:
    #             digits += str(i)
    #         print(f"Product group: {digits}")
    # else:
    #     print("Invalid barcode")
