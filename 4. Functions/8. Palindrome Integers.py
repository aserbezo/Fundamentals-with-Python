def palindrome(numbers):
    boole_value = []
    for i in numbers:
        current = i
        reverse_list = []
        for j in current:

            reverse_list.append(j)
        reverse_list.reverse()
        final =  "".join(reverse_list)
        if final == current:
            boole_value.append("True")
        else:
            boole_value.append("False")
    return ("\n".join(boole_value))

list_of_positive_numbers = input().split(", ")
print(palindrome(list_of_positive_numbers))

