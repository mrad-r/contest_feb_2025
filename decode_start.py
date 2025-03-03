from itertools import count

alphabet = " abcdefghijklmnopqrstuvwxyz"
vowel = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
        # print(line) #instead of print, you should start decoding
        num_vowels = 0
        for letter in line:
            if letter in vowel: #letter is a vowel
                num_vowels += 1

        message += alphabet[num_vowels]
    print(message)











