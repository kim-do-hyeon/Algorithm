# 백준 2576 - 홀수

A = [int(input()) for _ in range(7)]
odd = []
for i in A :
    if i % 2 == 1 :
        odd.append(i)

if len(odd) > 0 :
    print(sum(odd))
    print(min(odd))
else :
    print(-1)