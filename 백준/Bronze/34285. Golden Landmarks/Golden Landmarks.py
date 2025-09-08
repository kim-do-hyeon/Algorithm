# 백준 34285 - Golden Landmarks

def calc(start, end) :
    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]
    return abs(x1 - x2) + abs(y1 - y2)
N = int(input())
citys = {}
for _ in range(N) :
    s = input().split()
    city = s[0]
    x, y = int(s[1]), int(s[2])
    citys[city] = [x, y]

result = 0
walks = input().split()
curr_x, curr_y = citys[walks[0]][0], citys[walks[0]][1]
for i in range(1, len(walks)) :
    result += calc([curr_x, curr_y], citys[walks[i]])
    curr_x, curr_y = citys[walks[i]][0], citys[walks[i]][1]
print(result)