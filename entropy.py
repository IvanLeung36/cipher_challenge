import math
import string

entropy = 0
alphabets = dict.fromkeys(string.ascii_uppercase, 0)
text = input("Please input the text: ")
for char in text:
    if char in alphabets:
        alphabets[char] += 1
for alpha in alphabets:
    if alphabets[alpha] > 0:
        freq = alphabets[alpha] / len(text)
        entropy += freq * math.log(freq, 26)

print(-entropy)