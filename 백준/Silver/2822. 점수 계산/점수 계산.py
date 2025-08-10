# 백준 2822 - 점수 계산

A = [int(input()) for _ in range(8)]

X = sorted(A, reverse=True)

scores = []
indexs = []
for index, value in enumerate(X) :
    if index > 4 :
        break
    scores.append(value)
    indexs.append(A.index(value) + 1)
indexs = sorted(indexs)
print(sum(scores))
for i in indexs :
    print(i, end = " ")