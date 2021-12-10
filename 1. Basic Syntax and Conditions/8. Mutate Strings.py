first = input()
second = input()

last_string = first
for i_index in range(len(first)): # range (0, len(first))
    left = second[:i_index + 1]
    right = first[i_index + 1:]
    current_string = left + right
    if current_string == last_string:
        continue
    print(current_string)
    last_string =current_string
