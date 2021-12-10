
def character_in_range(star , end):
    symbols = []
    for char in range(ord(star) + 1, ord(end)):
        symbols.append(chr(char))
    return  symbols



first_char = input()
second_char = input()
result = character_in_range(first_char, second_char)
print(" ".join(result))