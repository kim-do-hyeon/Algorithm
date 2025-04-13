# 백준 1484 - 다이어트
# 분류 : 수학 / 투 포인터

G = int(input())

a = 1
b = 2
answers = []

while b <= 100000:  # 100,000^2 - 1^2 = 충분히 커짐
    diff = b * b - a * a

    if diff == G:
        answers.append(b)
        b += 1
    elif diff < G:
        b += 1
    else:
        a += 1

if answers:
    for ans in answers:
        print(ans)
else:
    print(-1)