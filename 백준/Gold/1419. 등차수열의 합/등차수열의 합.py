# 백준 1419 - 등차수열의 합
# 분류 : 수학

l = int(input())
r = int(input())
k = int(input())

if k == 2 :
    upper = max(0, r - 2)
    lower = max(0, l - 3)
    print(upper - lower)
elif k == 3 :
    upper = max(0, r // 3 - 1)
    lower = max(0, (l - 1) // 3 - 1)
    print(upper - lower)
elif k == 4 :
    upper = max(0, r // 2 - 4)
    lower = max(0, (l - 1) // 2 - 4)

    if r >= 12 :
        upper -= 1
    if l - 1 >= 12 :
        lower -= 1
    print(upper - lower)
else :
    upper = max(0, r // 5 - 2)
    lower = max(0, (l - 1) // 5 - 2)
    print(upper - lower)
