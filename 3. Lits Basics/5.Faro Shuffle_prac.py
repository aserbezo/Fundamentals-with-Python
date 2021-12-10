single_string = input().split()
shuffle_count = int(input())
deck_after_shuffle = []

for i in range(shuffle_count):
    deck_after_shuffle = []
    split_half_deck = len(single_string) // 2
    left = single_string[0:split_half_deck]
    right = single_string[split_half_deck::]
    for element in range(len(left)):
        deck_after_shuffle.append(left[element])
        deck_after_shuffle.append(right[element])
    single_string = deck_after_shuffle

print(deck_after_shuffle)