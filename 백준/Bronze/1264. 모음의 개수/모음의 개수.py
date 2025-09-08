# 백준 1264 - 모음의 개수

moum = ["a", "e", "i", "o", "u"]
while True :
    result = 0
    S = list(input())
    if S == ["#"] :
        break
    for i in S :
        if i.lower() in moum :
            result += 1
    print(result)