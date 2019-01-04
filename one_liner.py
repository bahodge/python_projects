word = list("cookies")

# print(word)
joined_word = "".join(word)

new_word = []
for char in word[:2:-1]:
    new_word.append(char)

print(new_word)
print(word)

# word.reverse()
# print(word)
# print(joined_word)
