# 백준 2745 - 진법 변환
# 분류 : 수학

inputs = input().split()
N = inputs[0]
B = int(inputs[1])
digit = len(N)
result = 0
for i in range(digit) :
    check = N[i]
    if 'A' <= check <= 'Z' :
        result += int((ord(check) - 55)) * (B ** (digit - i - 1))
    else :
        result += int(check) * (B ** (digit -i - 1))
print(result)