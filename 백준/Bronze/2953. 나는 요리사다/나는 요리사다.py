# 백준 2953 - 나는 요리사다

scores = []
for _ in range(5) :
    scores.append(sum(list(map(int, input().split()))))

print(scores.index(max(scores)) + 1, max(scores))