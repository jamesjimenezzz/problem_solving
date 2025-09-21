letters = "abcdefg"

result = []

for i in range (0, len(letters), 2):
    if len(letters) % 2 != 0:
        letters += "_"

    result.append(letters[i:i + 2])


print(result)