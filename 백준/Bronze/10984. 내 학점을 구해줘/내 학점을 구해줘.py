# 백준 10984 - 내 학점을 구해줘

T = int(input())
for _ in range(T) :
    N = int(input())
    grades = 0
    total_scores = 0
    for i in range(N) :
        data = input().split()
        grade = int(data[0])
        score = float(data[1])
        grades += grade
        total_scores += (score * grade)
    print(grades, round(total_scores / grades, 1))
    