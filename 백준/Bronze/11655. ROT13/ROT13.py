# 백준 11655 - ROT13
S = list(input())
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
for i in S :
    if i in alphabet :
        calc = ord(i) + 13
        if calc > 122 and i.islower() :
            calc = calc - 26
        elif calc > 90 and i.isupper():
            calc = calc - 26
        print(chr(calc), end = "")
    else :
        print(i, end = "")