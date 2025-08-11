# 백준 10987 - 모음의 개수

moun = ["a", "e", "i", "o", "u"]
S = list(input())
result = 0
for i in S :
    if i in moun :
        result += 1

print(result)