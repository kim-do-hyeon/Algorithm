# 백준 3197 - 백조의 호수
# 분류 : BFS
# 문제집 : 단기간 성장 - 3번

R, C = map(int, input().split())
A = [list(input()) for _ in range(R)]

# 1. 백조 위치 확인
swans = []
for i in range(R) :
    for j in range(C) :
        if A[i][j] == "L" :
            swans.append((i, j))
        if len(swans) == 2 :
            break
    if len(swans) == 2 :
        break

swan_1, swan_2 = swans

# 2. 현재 물 찾기
from collections import deque

water = deque()
visit_water = [[False] * C for _ in range(R)]

for i in range(R) :
    for j in range(C) :
        if A[i][j] != "X" :
            water.append((i, j))
            visit_water[i][j] = True

# 3. 백조 이동 BFS 준비
swan_q = deque()
next_swan_q = deque()
visit_swan = [[False] * C for _ in range(R)]
swan_q.append(swan_1)
visit_swan[swan_1[0]][swan_1[1]] = True

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def swan_move() :
    while swan_q :
        x, y = swan_q.popleft()
        for dx, dy in directions :
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C) :
                continue
            if visit_swan[nx][ny] == True :
                continue
            visit_swan[nx][ny] = True
            if (nx, ny) == swan_2 :
                return True
            if A[nx][ny] == '.' :
                swan_q.append((nx, ny))
            elif A[nx][ny] == 'X' :
                next_swan_q.append((nx, ny))
    return False

def melt() :
    for _ in range(len(water)) :
        x, y = water.popleft()
        for dx, dy in directions :
            nx, ny = x + dx, y + dy
            if not (0 <= nx < R and 0 <= ny < C) :
                continue
            if visit_water[nx][ny] :
                continue
            if A[nx][ny] == 'X' :
                A[nx][ny] = '.'
                water.append((nx, ny))
                visit_water[nx][ny] = True

# 4. 시뮬레이션
day = 0
while True :
    if swan_move() :
        print(day)
        break
    melt()
    swan_q, next_swan_q = next_swan_q, deque()
    day += 1