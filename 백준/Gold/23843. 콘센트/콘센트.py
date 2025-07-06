import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))

# 시간이 긴 순서대로 정렬
A.sort(reverse=True)

# 각 콘센트의 누적 사용 시간 (우선순위 큐)
pq = [0] * M
heapq.heapify(pq)

for time in A:
    min_time = heapq.heappop(pq)      # 가장 짧게 쓰고 있는 콘센트
    heapq.heappush(pq, min_time + time)  # 이 콘센트에 현재 기기 추가

print(max(pq))  # 가장 오래 걸리는 콘센트가 총 걸린 시간