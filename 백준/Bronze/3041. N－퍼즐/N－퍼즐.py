puzzle = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
puzzle2 = []
pos = {}
cnt = 0
for _ in range(4):
    puzzle2.append(input())

for i in range(4):
    for j in range(4):
        if puzzle[i][j] != puzzle2[i][j] and puzzle2[i][j] != '.':
            pos[puzzle2[i][j]] = (i, j)

for i in range(4):
    for j in range(4):
        if puzzle[i][j] in pos.keys():
            cnt += abs(pos[puzzle[i][j]][0]-i) + abs(pos[puzzle[i][j]][1]-j)

print(cnt)