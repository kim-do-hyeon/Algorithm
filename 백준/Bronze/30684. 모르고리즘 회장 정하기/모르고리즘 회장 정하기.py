# 백준 30684 - 모르고리즘 회장 정하기
# 분류 : 구현

N = int(input())

candidate = []

for i in range(N) :
    name = input()
    if len(name) == 3 :
        candidate.append(name)

candidate.sort()

print(candidate[0])