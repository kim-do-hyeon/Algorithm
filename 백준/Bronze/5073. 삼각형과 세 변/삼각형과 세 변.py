# 백준 5073 - 삼각형과 세 변
# 단계별로 풀어보기 - 10 기하: 직사각형과 삼각형
# 분류 : 수학

while True :
    A, B, C = map(int, input().split())
    if A == 0 and B == 0 and C == 0 :
        break
    elif max([A, B, C]) >= sum([A, B, C]) - max([A, B, C]) :
        print("Invalid")
    elif max([A, B, C]) < sum([A, B, C]) - max([A, B, C]) :
        if A == B and B == C :
            print("Equilateral")
        elif A == B or B == C or A == C:
            print("Isosceles")
        elif A != B and B != C and A != C :
            print("Scalene")
    else :
        print("Invalid")
