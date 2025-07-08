import re
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = 10**9 + 1  # 1,000,000,001

# 1) 기본 재료 비용 저장
stuff = {}
for _ in range(N):
    name, cost = input().split()
    stuff[name] = int(cost)

# 2) 조합식 파싱 및 '–1'로 초기화
formulas = []
for _ in range(M):
    line = input().strip()
    result, expr = line.split("=")
    formulas.append((result, expr))
    if result not in stuff:
        stuff[result] = -1
    for e in expr.split("+"):
        k, nm = re.match(r"(\d+)([A-Z]+)", e).groups()
        if nm not in stuff:
            stuff[nm] = -1

# 3) 반복 업데이트
while True:
    updated = False
    for result, expr in formulas:
        total = 0
        computable = True

        # 각 재료 검사
        for e in expr.split("+"):
            k, nm = re.match(r"(\d+)([A-Z]+)", e).groups()
            k = int(k)
            cost_nm = stuff[nm]
            if cost_nm == -1:
                computable = False
                break

            # 비용 클램핑
            cost = k * cost_nm
            if cost > INF:
                cost = INF
            total += cost
            if total > INF:
                total = INF

        # 갱신 조건: 새로 만들 수 있고, 이전보다 싸거나 –1 이었다면
        if computable and (stuff[result] == -1 or total < stuff[result]):
            stuff[result] = total
            updated = True

    if not updated:
        break

# 4) 최종 출력
ans = stuff.get("LOVE", -1)
print(ans)