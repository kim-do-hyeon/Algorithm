# 백준 1100 - 하얀 칸
# 분류 : 구현

B = [input() for _ in range(8)]

answer = 0
for i in range(8) :
    for j in range(8) :
        if (i + j) % 2 == 0 and B[i][j] == 'F' :
            answer += 1

print(answer)