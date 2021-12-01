from itertools import product
from math import log2, ceil
from random import randint

word = input('Enter word please: ')
chars = [chr(char) for char in range(97, 123)]
codes = tuple(product(*[[0, 1]] * 5))
alphabet = {
    chars[idx]: codes[idx] for idx in range(26)
}

back_alphabet = {
    codes[idx]: chars[idx] for idx in range(26)
}

encoded = [alphabet[letter] for letter in word]
encoded = [item for sublist in encoded for item in sublist]

idx = [2 ** i - 1 for i in range(ceil(log2(len(encoded))) + 1)]
if idx[-1] >= len(encoded):
    del idx[-1]

for power in idx:
    encoded.insert(power, 0)

matrix = list(product(*[[0, 1]] * (len(idx))))
del matrix[0]

bits = []

for row in range(len(idx) - 1, -1, -1):
    counter = 0
    for col in range(len(encoded) - 1, -1, -1):
        counter += matrix[col][row] * encoded[col]
    bits.append(counter % 2)

for power in range(len(idx)):
    encoded[idx[power]] = bits[power]

bit_to_replace = randint(0, len(encoded) - 1)
encoded[bit_to_replace] = 1 - encoded[bit_to_replace]

bits_new = []
for row in range(len(idx) - 1, -1, -1):
    counter = 0
    for col in range(len(encoded) - 1, -1, -1):
        counter += matrix[col][row] * encoded[col]
    bits_new.append(counter % 2)

bad_bit = int(''.join(map(str, bits_new))[::-1], 2) - 1
encoded[bad_bit] = 1 - encoded[bad_bit]

final_array = []
for i in range(len(encoded)):
    if log2(i + 1) - int(log2(i + 1)) == 0:
        continue
    final_array.append(encoded[i])

final = ''.join(map(str, final_array))
decoded = ''
for i in range(0, len(final), 5):
    decoded += back_alphabet[tuple(final_array[i: i + 5])]

print(f'Decoded word: {decoded}')
