# 백준 10833 - 사과
N = int(input())
answers = 0
for _ in range(N) :
    student, apple = map(int, input().split())
    answers += (apple % student)
print(answers)