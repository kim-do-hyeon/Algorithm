# 백준 10821 - 정수의 개수

S = input().split(",")
result = 0
for i in S :
    if i.isdigit() == True :
        result += 1
print(result)