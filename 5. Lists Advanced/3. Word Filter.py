words = input().split()
print("\n".join(s for s in words if len(s) % 2 == 0))

# even_word = [ word for word in words if len(words) % 2 == 0]
# print("\n".join(even_word))