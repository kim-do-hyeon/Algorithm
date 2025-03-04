H, W = map(int, input().split())
A = list(map(int, input().split()))

# 왼쪽 최대 높이 배열
left_max = [0] * W
left_max[0] = A[0]
for i in range(1, W):
    left_max[i] = max(left_max[i - 1], A[i])

# 오른쪽 최대 높이 배열
right_max = [0] * W
right_max[W - 1] = A[W - 1]
for i in range(W - 2, -1, -1):
    right_max[i] = max(right_max[i + 1], A[i])

# 빗물 계산
rainwater = 0
for i in range(W):
    rainwater += max(0, min(left_max[i], right_max[i]) - A[i])

print(rainwater)