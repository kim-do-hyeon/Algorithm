# 백준 1931 - 회의실 배정
# 분류 : 그리디

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

A.sort(key = lambda x : (x[1], x[0]))

answer = 0
end_point = 0
for start, end in A :
    if end_point <= start :
        answer += 1
        end_point = end

print(answer)