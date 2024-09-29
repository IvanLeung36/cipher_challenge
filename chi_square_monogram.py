from chi_squared import chi_square
from collections import Counter
frequencies = {
    "a": 8.167,
    "b": 1.492,
    "c": 2.782,
    "d": 4.253,
    "e": 12.702,
    "f": 2.228,
    "g": 2.015,
    "h": 6.094,
    "i": 6.966,
    "j": 0.153,
    "k": 0.772,
    "l": 4.025,
    "m": 2.406,
    "n": 6.749,
    "o": 7.507,
    "p": 1.929,
    "q": 0.095,
    "r": 5.987,
    "s": 6.327,
    "t": 9.056,
    "u": 2.758,
    "v": 0.978,
    "w": 2.360,
    "x": 0.150,
    "y": 1.974,
    "z": 0.074
} #Source: https://gist.github.com/evilpacket/5973230

def monogram_fitness(text, ignore_spaces=True, use_reciprocal=True):
    if ignore_spaces:
        text = ''.join(filter(str.isalpha, text)).lower()

    length = len(text)
    
    if length == 0:
        return float('inf') if use_reciprocal else 0
    
    observed_frequency = Counter(text)
    observed = [(observed_frequency[char] / length) * 100 for char in frequencies]
    expected = [frequencies[char] for char in frequencies]
    chi_s = chi_square(observed, expected)

    if use_reciprocal:
        return 1 / chi_s if chi_s != 0 else float('inf')
    else:
        return -chi_s
fitness = monogram_fitness(input("Text: "))
print(fitness)