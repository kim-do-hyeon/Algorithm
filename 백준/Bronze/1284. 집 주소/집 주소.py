# 백준 1284 - 집 주소

# 1 -> 2cm, 0 -> 4cm, etc -> 3cm / split -> 1cm

while True :
    S = list(input())
    if S == ["0"] :
        quit()
    result = 1
    for i in S :
        if i == "1" :
            result += 2
        elif i == "0" :
            result += 4
        else :
            result += 3
        result += 1

    print(result)