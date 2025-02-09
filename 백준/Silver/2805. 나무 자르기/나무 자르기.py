import sys

input = sys.stdin.readline

N, M = map(int, input().split())
heights = list(map(int, input().split()))

start, end = 0, max(heights)

# 정렬하여 이분 탐색에 활용
heights.sort()

answer = 0
while start <= end:
    mid = (start + end) // 2
    
    # 잘린 나무의 총 길이 계산 (이진 탐색 활용)
    total = sum(h - mid for h in heights if h > mid)

    if total >= M:
        answer = mid  # 현재 높이 저장 (조건 충족)
        start = mid + 1  # 더 높은 높이 시도
    else:
        end = mid - 1  # 높이를 낮춰야 함

print(answer)
