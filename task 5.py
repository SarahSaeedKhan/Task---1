def conversion_strings(S: str):
    words = S.split()
    for x in range(len(words)):
        words[x] = words[x][1:] + words[x][0] + 'ay'

    print(" ".join(words))


S = input('enter the string for the conversion')
print(S)
conversion_strings(S)

