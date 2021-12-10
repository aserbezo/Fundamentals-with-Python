
string = input()

text = input()

while text != "Done":
    data = text.split()
    if data[0] == "Change":
        char , replacement = data[1:]
        string = string.replace(char,replacement)
        print(string)
    elif data[0] == "Includes":
        substring = data[1]
        if substring in string:
            print("True")
        else:
            print("False")
    elif data[0]== "End":
        substring_end = data[1]
        if substring_end == string[-1]:
            print("True")
        else:
            print("False")
    elif data[0] == "Uppercase":
        string = string.upper()
        print(string)
    elif data[0] == "FindIndex":
        char = data[1]
        for el in range(len(string)):
            if string[el] == char:
                print(el)
                break
    elif data[0] == "Cut":
        start_index , count = data[1:]
        start_index = int(start_index)
        count = int(count)
        string = string[start_index::]
        new_text = string[0:count]
        print(new_text)

    text = input()