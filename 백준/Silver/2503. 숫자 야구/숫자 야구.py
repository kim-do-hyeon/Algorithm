# 백준 2503 - 숫자 야구
# 분류 : 브루트포스

from itertools import permutations

N = int(input())

qna = []

for _ in range(N) :
    qna.append(input().split())

count = 0
for permutation in permutations(range(1, 10), 3) :
    good = True
    for i in range(len(qna)) :
        strike = 0
        ball = 0
        for j in range(3) :
            if int(qna[i][0][j]) == permutation[j] :
                strike += 1
                continue
            if int(qna[i][0][j]) in permutation :
                ball += 1
        
        if strike != int(qna[i][1]) :
            good = False
        if ball != int(qna[i][2]) :
            good = False

    if good :
        count += 1

print(count)