words = input().split(" ")
dictionary = {}

# Create a loop and check for each word (lower case) if it is in the dictionary, and if it is not, add it:

for word in words:
    word_lower = word.lower()
    if word_lower not in dictionary:
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

#Then create another loop using the items() method and check if the occurrence of the current word is odd

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")