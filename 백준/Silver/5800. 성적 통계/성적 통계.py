# 백준 5800 - 성적 통계

K = int(input())
for i in range(K) :
    A = list(map(int, input().split()))
    N = A[0]
    scores = A[1:]
    max_value = max(scores)
    min_value = min(scores)
    print(f"Class {i + 1}")
    sort_scores = sorted(scores, reverse=True)
    max_gap = 0
    for j in range(1, len(sort_scores)) :
        max_gap = max(sort_scores[j - 1] - sort_scores[j], max_gap)
    print(f"Max {max_value}, Min {min_value}, Largest gap {max_gap}")