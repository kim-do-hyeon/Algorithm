# 백준 11557 - Yangjojang of The Year
# 문제집 : Python 배우기 (1 ~ 50)

T = int(input())
# dict가 효율적일까? 리스트가 효율적일까
for _ in range(T) :
    N = int(input())
    names = []
    scores = []
    for i in range(N) :
        S = input().split()
        name, score = S[0], int(S[1])
        names.append(name)
        scores.append(score)
    print(names[scores.index(max(scores))])