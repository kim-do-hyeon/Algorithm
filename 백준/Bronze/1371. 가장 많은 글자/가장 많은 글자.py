# 백준 1371 - 가장 많은 글자

import sys
text = sys.stdin.read()
alphabet = {}
alphabet_lists = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet_lists :
    alphabet[i] = 0

for char in text :
    if char in alphabet :
        alphabet[char] += 1

max_scores = max(alphabet.values())
for key, value in alphabet.items() :
    if value == max_scores :
        print(key, end = "")