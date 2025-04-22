# 백준 10101 - 삼각형 외우기
# 단계별로 풀어보기 - 10 기하: 직사각형과 삼각형
# 분류 : 수학

angles = []
for i in range(3) :
    angles.append(int(input()))

if sum(angles) != 180 :
    print("Error")
elif len(list(set(angles))) == 1 and sum(angles) == 180 :
    print("Equilateral")
elif len(list(set(angles))) == 2 and sum(angles) == 180 :
    print("Isosceles")
elif len(list(set(angles))) == 3 and sum(angles) == 180 :
    print("Scalene")