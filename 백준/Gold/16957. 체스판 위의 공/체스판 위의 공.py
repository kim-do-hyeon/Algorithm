import sys
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R)]

dr = [0, 0, 1, 1, 1, -1, -1, -1]
dc = [1, -1, -1, 0, 1, -1, 0, 1]

# 각 칸이 최종적으로 흘러가는 지점을 저장
dest = [[(-1, -1) for _ in range(C)] for _ in range(R)]

def find_dest(r, c):
    if dest[r][c] != (-1, -1):
        return dest[r][c]
    
    min_val = B[r][c]
    min_pos = (r, c)

    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if B[nr][nc] < min_val:
                min_val = B[nr][nc]
                min_pos = (nr, nc)

    if min_pos == (r, c):
        dest[r][c] = (r, c)
    else:
        dest[r][c] = find_dest(*min_pos)
    
    return dest[r][c]

# 물이 모이는 지점별 개수 세기
result = [[0] * C for _ in range(R)]
for r in range(R):
    for c in range(C):
        tr, tc = find_dest(r, c)
        result[tr][tc] += 1

# 출력
for row in result:
    print(*row)