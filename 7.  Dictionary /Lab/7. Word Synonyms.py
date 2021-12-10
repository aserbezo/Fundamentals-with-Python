n = int(input())
synonyms = {}

# Then we create a for loop to read the word-synonym pairs:

for i in range(n):
    word = input()
    given_synonym = input()

#We check if the word is not in the dictionary, and in that case, we set its value to an empty list
# (since one word can have multiple synonyms), and we append the new synonym to that list:
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(given_synonym)

for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")